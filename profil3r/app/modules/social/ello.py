import requests
from bs4 import BeautifulSoup
import time
import re

class Ello:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['ello']['rate_limit'] / 1000
        # https://ello.co/{username}
        self.format = config['plateform']['ello']['format']
        self.permutations_list = permutations_list
        # Social
        self.type = config['plateform']['ello']['type']

    # Generate all potential ello usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        ello_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username, timeout=5)
            except requests.ConnectionError:
                print("failed to connect to ello")
            
            # If the account exists
            if r.status_code == 200:
                ello_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        return ello_usernames