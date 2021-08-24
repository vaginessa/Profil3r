from profil3r.app.search import search_get
import time

class Disqus:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['disqus']['rate_limit'] / 1000
        # https://disqus.com/by/{username}
        self.format = config['plateform']['disqus']['format']
        # disqus usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # Social
        self.type = config['plateform']['disqus']['type']

    # Generate all potential disqus usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        disqus_usernames = {
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
                disqus_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return disqus_usernames