from profil3r.app.search import search_get

import time
import re

class Ifttt:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['ifttt']['rate_limit'] / 1000
        # https://ifttt.com/p/{username}
        self.format = config['plateform']['ifttt']['format']
        self.permutations_list = permutations_list
        # Social
        self.type = config['plateform']['ifttt']['type']

    # Generate all potential ifttt usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        ifttt_usernames = {
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
                ifttt_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        return ifttt_usernames