from profil3r.app.search import search_get
import time

class Redtube:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['redtube']['rate_limit'] / 1000
        # https://fr.redtube.com/users/{username}
        self.format = config['plateform']['redtube']['format']
        # Redtube usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # Porn
        self.type = config['plateform']['redtube']['type']

    # Generate all potential redtube usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        redtube_usernames = {
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
                redtube_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return redtube_usernames