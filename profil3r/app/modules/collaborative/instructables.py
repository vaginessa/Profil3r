import requests
from bs4 import BeautifulSoup
import time
import re

class Instructables:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['instructables']['rate_limit'] / 1000
        # https://www.instructables.com/members/{username}
        self.format = config['plateform']['instructables']['format']
        self.permutations_list = permutations_list
        # Collaborative
        self.type = config['plateform']['instructables']['type']

    # Generate all potential root-me usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        instructables_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username, timeout=5)
            except requests.ConnectionError:
                print("failed to connect to instructables")
            
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
                    user_username = str(soup.find_all('h1', {'class':'profile-title'})[0].get_text()) if soup.find_all('h1', {'class':'profile-title'}) else None
                    user_location = str(soup.find_all('span', {'class':'stat-text member-location'})[0].get_text()) if soup.find_all('span', {'class':'stat-text member-location'}) else None
                    user_account_creation_date = str(soup.find_all('span', {'class':'stat-text member-signup-date'})[0].get_text()).replace("Joined ", "") if soup.find_all('span', {'class':'stat-text member-signup-date'}) else None

                    account["username"] = {"name": "Username", "value": user_username}
                    account["location"] = {"name": "Location", "value": user_location}
                    account["creation_date"] = {"name": "Account Creation", "value": user_account_creation_date}
                except:
                    pass
                
                # Append the account to the accounts table
                instructables_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return instructables_usernames