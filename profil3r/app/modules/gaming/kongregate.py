from profil3r.app.search import search_get
from bs4 import BeautifulSoup
import time

class Kongregate:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['kongregate']['rate_limit'] / 1000
        # https://www.kongregate.com/accounts/{username}}
        self.format = config['plateform']['kongregate']['format']
        # Kongregate usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # Gaming
        self.type = config['plateform']['kongregate']['type']

    # Generate all potential kongregate usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        kongregate_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            r = search_get(username)
            if not r:
                continue
            
            # If the account exists
            if r.status_code == 200:
                # Account object
                account = {}

                # Get the username
                account["value"] = username
                
                # Parse HTML response content with beautiful soup 
                soup = BeautifulSoup(r.text, 'html.parser')
                
                # Scrape the user informations
                try:
                    user_username = str(soup.find_all(class_="mbn")[0].get_text()) if soup.find_all(class_="mbn") else None
                    user_account_creation_date = str(soup.find_all(class_="prm")[0].get_text()) if soup.find_all(class_="prm") else None
                    user_badges_count = str(soup.find_all(class_="user_metric_stat")[2].get_text()) if soup.find_all(class_="user_metric_stat") else None
                    user_comments_count = str(soup.find_all(class_="user_metric_stat")[3].get_text()) if soup.find_all(class_="user_metric_stat") else None
                    user_favorites_count = str(soup.find_all(class_="user_metric_stat")[4].get_text()) if soup.find_all(class_="user_metric_stat") else None
                    user_forum_posts_count = str(soup.find_all(class_="user_metric_stat")[5].get_text()) if soup.find_all(class_="user_metric_stat") else None
                    user_fans_count = str(soup.find_all(class_="user_metric_stat")[6].get_text()) if soup.find_all(class_="user_metric_stat") else None
                    user_friends_count = str(soup.find_all(class_="user_metric_stat")[7].get_text()) if soup.find_all(class_="user_metric_stat") else None
                    user_level = str(soup.find_all(class_="user_metric_stat")[0].get_text()) if soup.find_all(class_="user_metric_stat") else None
                    user_points = str(soup.find_all(class_="user_metric_stat")[1].get_text()) if soup.find_all(class_="user_metric_stat") else None


                    account["username"] = {"name": "Username", "value": user_username}
                    account["account_creation_date"] = {"name": "Account Creation", "value": user_account_creation_date}
                    account["badges_count"] = {"name": "Badges", "value": user_badges_count}
                    account["comments_count"] = {"name": "Comments", "value": user_comments_count}
                    account["favorites_count"] = {"name": "Favorites", "value": user_favorites_count}
                    account["forum_posts_count"] = {"name": "Posts", "value": user_forum_posts_count}
                    account["fans_count"] = {"name": "Fans", "value": user_fans_count}
                    account["friends_count"] = {"name": "Friends", "value": user_friends_count}
                    account["level"] = {"name": "Level", "value": user_level}
                    account["points"] = {"name": "Points", "value": user_points}

                except:
                    pass
                
                # Append the account to the accounts table
                kongregate_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return kongregate_usernames