from profil3r.app.search import search_get
from bs4 import BeautifulSoup
import time
import re

class Keybase:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['keybase']['rate_limit'] / 1000
        # https://keybase.io/{username}
        self.format = config['plateform']['keybase']['format']
        self.permutations_list = permutations_list
        # Privacy
        self.type = config['plateform']['keybase']['type']

    # Generate all potential keybase usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        keybase_usernames = {
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
                    user_key_fingerprint = str(soup.find_all(class_='pgp-fingerprint')[0].get_text())if soup.find_all(class_='pgp-fingerprint') else None
                    # Format key fingerprint
                    user_key_fingerprint = ' '.join([user_key_fingerprint[i:i+4] for i in range(0, len(user_key_fingerprint), 4)])

                    account["key_fingerprint"] = {"name": "Key Fingerprint", "value": user_key_fingerprint}
                except:
                    pass
                
                # Append the account to the accounts table
                keybase_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return keybase_usernames