from profil3r.app.search import search_get
from bs4 import BeautifulSoup
import time
import re

class Tripadvisor:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['tripadvisor']['rate_limit'] / 1000
        # https://www.tripadvisor.com/Profile/{username}
        self.format = config['plateform']['tripadvisor']['format']
        self.permutations_list = permutations_list
        # Travel
        self.type = config['plateform']['tripadvisor']['type']

    # Generate all potential tripadvisor usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        tripadvisor_usernames = {
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
                tripadvisor_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        return tripadvisor_usernames