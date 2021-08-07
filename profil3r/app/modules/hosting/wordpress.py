from profil3r.app.search import search_get
import time

class Wordpress:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['wordpress']['rate_limit'] / 1000
        # https://{username}.wordpress.com
        self.format = config['plateform']['wordpress']['format']
        # Wordpress usernames are not case sensitive
        self.permutations_list = permutations_list
        # Hosting
        self.type = config['plateform']['wordpress']['type']

    # Generate all potential wordpress usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        wordpress_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            r = search_get(username)
            if not r:
                continue
            
            # If the account exists
            if "Do you want to register" not in r.text:
                wordpress_usernames["accounts"].append({"value": username})

            time.sleep(self.delay)
        
        return wordpress_usernames