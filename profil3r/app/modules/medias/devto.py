from profil3r.app.search import search_get
from bs4 import BeautifulSoup
import time

class Devto:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['devto']['rate_limit'] / 1000
        # https://dev.to/{username}
        self.format = config['plateform']['devto']['format']
        self.permutations_list = permutations_list
        # Hosting
        self.type = config['plateform']['devto']['type']

    # Generate all potential devto usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        devto_usernames = {
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
                devto_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        return devto_usernames