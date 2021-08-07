from profil3r.app.search import search_get
from bs4 import BeautifulSoup
import time

class Hubpages:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['hubpages']['rate_limit'] / 1000
        # https://hubpages.com/@{username}
        self.format = config['plateform']['hubpages']['format']
        self.permutations_list = permutations_list
        # Medias
        self.type = config['plateform']['hubpages']['type']

    # Generate all potential hubpages usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        hubpages_usernames = {
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
                    user_username = str(soup.find_all(class_="author_primary_name")[0].get_text()) if soup.find_all(class_="name") else None
                    user_articles_count = str(soup.find_all("div", {"class": "value"})[0].get_text()) if soup.find_all("div", {"class": "value"}) else None
                    user_followers_count = str(soup.find_all("div", {"class": "value"})[1].get_text()) if soup.find_all("div", {"class": "value"}) else None
                    user_following_count = str(soup.find_all("div", {"class": "value"})[2].get_text()) if soup.find_all("div", {"class": "value"}) else None

                    account["username"] = {"name": "Username", "value": user_username}
                    account["articles_count"] = {"name": "Articles", "value": user_articles_count}
                    account["followers_count"] = {"name": "Followers", "value": user_followers_count}
                    account["following_count"] = {"name": "Following", "value": user_following_count}

                except:
                    pass
                
                # Append the account to the accounts table
                hubpages_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return hubpages_usernames