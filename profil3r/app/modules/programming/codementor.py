import requests
from bs4 import BeautifulSoup
import time

class Codementor:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['codementor']['rate_limit'] / 1000
        # https://www.codementor.io/@{username}
        self.format = config['plateform']['codementor']['format']
        self.permutations_list = permutations_list
        # Programming
        self.type = config['plateform']['codementor']['type']

    # Generate all potential codementor usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        codementor_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username, timeout=5)
            except requests.ConnectionError:
                print("failed to connect to codementor")
            
            # If the account exists
            if r.status_code == 200:
                codementor_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        return codementor_usernames