import requests
from bs4 import BeautifulSoup
import time

class Bandcamp:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['bandcamp']['rate_limit'] / 1000
        # https://bandcamp.com/{username}
        self.format = config['plateform']['bandcamp']['format']
        self.permutations_list = permutations_list
        # music
        self.type = config['plateform']['bandcamp']['type']

    # Generate all potential bandcamp usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        bandcamp_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username, timeout=5)
            except requests.ConnectionError:
                print("failed to connect to bandcamp")
            
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
                    user_username = str(soup.find_all("div", {"class": "name"})[0].find("h1").get_text()) if soup.find_all("div", {"class": "name"}) else None
                    user_music_gender = str(soup.find_all("li", {"class": "genre-wrapper"})[0].get_text()) if soup.find_all("li", {"class": "genre-wrapper"}) else None
                    user_website = str(soup.find_all("div", {"class": "website wide"})[0].get_text()) if soup.find_all("div", {"class": "website wide"}) else None

                    account["username"] = {"name": "Username", "value": user_username}
                    account["music_gender"] = {"name": "Musical Gender", "value": user_music_gender}
                    account["website"] = {"name": "Website", "value": user_website}
                except:
                    pass
                
                # Append the account to the accounts table
                bandcamp_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return bandcamp_usernames