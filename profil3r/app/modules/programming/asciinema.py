import requests
import time

class Asciinema:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['asciinema']['rate_limit'] / 1000
        # https://asciinema.org/~{username}
        self.format = config['plateform']['asciinema']['format']
        # asciinema usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # programming
        self.type = config['plateform']['asciinema']['type']

    # Generate all potential asciinema usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        asciinema_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username)
            except requests.ConnectionError:
                print("failed to connect to asciinema")
            
            # If the account exists
            if r.status_code == 200:
                asciinema_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return asciinema_usernames