import requests
from bs4 import BeautifulSoup
import time

class Pypi:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['pypi']['rate_limit'] / 1000
        # https://pypi.org/user/{username}
        self.format = config['plateform']['pypi']['format']
        self.permutations_list = permutations_list
        # Programming
        self.type = config['plateform']['pypi']['type']

    # Generate all potential pypi usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        pypi_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username, timeout=5)
            except requests.ConnectionError:
                print("failed to connect to pypi")
            
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
                    user_full_name = str(soup.find_all(class_='author-profile__name')[0].get_text()) if soup.find_all(class_='author-profile__name') else None
                    user_account_creation_date = str(soup.find_all('time')[0].get_text()) if soup.find_all('time') else None

                    account["full_name"] = {"name": "Full Name", "value": user_full_name}
                    account["account_creation_date"] = {"name": "Account Creation", "value": user_account_creation_date}
                except:
                    pass
                
                # Append the account to the accounts table
                pypi_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return pypi_usernames