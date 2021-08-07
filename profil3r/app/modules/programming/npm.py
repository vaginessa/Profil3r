from profil3r.app.search import search_get
from bs4 import BeautifulSoup
import time
import re

class Npm:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['npm']['rate_limit'] / 1000
        # https://www.npmjs.com/~{username}
        self.format = config['plateform']['npm']['format']
        self.permutations_list = permutations_list
        # Programming
        self.type = config['plateform']['npm']['type']

    # Generate all potential npm usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        npm_usernames = {
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
                    user_full_name = str(soup.find_all(class_='black-50 mv2')[0].get_text()) if soup.find_all(class_='black-50 mv2') else None
                    user_package_count = str(soup.find_all(class_='c3fc8940')[0].get_text()) if soup.find_all(class_='c3fc8940') else None
                    user_organization_count = str(soup.find_all(class_='c3fc8940')[1].get_text()) if soup.find_all(class_='c3fc8940') else None
                    user_github_account = str(soup.find_all('a', href = re.compile(r'https:\/\/github\.com.*'))[0].get_text()) if soup.find_all('a', href = re.compile(r'https:\/\/github\.com.*')) else None

                    account["full_name"] = {"name": "Full Name", "value": user_full_name}
                    account["packages_count"] = {"name": "Packages", "value": user_package_count}
                    account["organizations_count"] = {"name": "Organizations", "value": user_organization_count}
                    account["github_account"] = {"name": "Github", "value": user_github_account}
                except:
                    pass
                
                # Append the account to the accounts table
                npm_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return npm_usernames