from profil3r.app.search import search_get
import time

class Crackedto:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['crackedto']['rate_limit'] / 1000
        # https://cracked.to/{username}
        self.format = config['plateform']['crackedto']['format']
        self.permutations_list = permutations_list
        # Forum
        self.type = config['plateform']['crackedto']['type']

    # Generate all potential cracked.to usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        cracked_usernames = {
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
                cracked_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return cracked_usernames