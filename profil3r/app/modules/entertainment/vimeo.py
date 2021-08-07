from profil3r.app.search import search_get
import time

class Vimeo:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['vimeo']['rate_limit'] / 1000
        # https://vimeo.com/{username}
        self.format = config['plateform']['vimeo']['format']
        self.permutations_list = permutations_list
        # entertainment
        self.type = config['plateform']['vimeo']['type']

    # Generate all potential vimeo usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        vimeo_usernames = {
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
                vimeo_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return vimeo_usernames