from profil3r.app.search import search_get
from bs4 import BeautifulSoup
import time

class Dribbble:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['dribbble']['rate_limit'] / 1000
        # https://dribbble.com/{username}/about
        self.format = config['plateform']['dribbble']['format']
        # Dribbble usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # Entertainment
        self.type = config['plateform']['dribbble']['type']

    # Generate all potential dribbble usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        dribbble_usernames = {
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
                    user_username = str(soup.find_all(class_="masthead-profile-name")[0].get_text()) if soup.find_all(class_="masthead-profile-name") else None
                    user_shots_count = str(soup.find_all(class_="count")[0].get_text()) if soup.find_all(class_="count") else None
                    user_collections_count = str(soup.find_all(class_="count")[1].get_text()) if soup.find_all(class_="count") else None
                    user_liked_shots_count = str(soup.find_all(class_="count")[2].get_text()) if soup.find_all(class_="count") else None
                    user_followers_count = str(soup.find_all(class_="count")[3].get_text()) if soup.find_all(class_="count") else None
                    user_following_count = str(soup.find_all(class_="count")[4].get_text()) if soup.find_all(class_="count") else None
                    user_tags_count = str(soup.find_all(class_="count")[5].get_text()) if soup.find_all(class_="count") else None
                    user_location = str(soup.find_all(class_="location")[0].get_text()) if soup.find_all(class_="location") else None
                    user_creation_date = str(soup.find_all(class_="created")[0].get_text()).replace("Member since ", "") if soup.find_all(class_="info-item created") else None

                    account["username"] = {"name": "Username", "value": user_username}
                    account["shots_count"] = {"name": "Shots", "value": user_shots_count}
                    account["collections_count"] = {"name": "Collections", "value": user_collections_count}
                    account["liked_shots_count"] = {"name": "Liked Shots", "value": user_liked_shots_count}
                    account["followers_count"] = {"name": "Followers", "value": user_followers_count}
                    account["following_count"] = {"name": "Following", "value": user_following_count}
                    account["tags_count"] = {"name": "tags", "value": user_tags_count}
                    account["location"] = {"name": "Location", "value": user_location}
                    account["creation_date"] = {"name": "Account Creation", "value": user_creation_date}
                except:
                    pass
                
                # Append the account to the accounts table
                dribbble_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return dribbble_usernames