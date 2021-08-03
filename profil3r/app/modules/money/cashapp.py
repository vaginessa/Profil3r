import requests
import time

class Cashapp:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['cashapp']['rate_limit'] / 1000
        # https://cash.app/${username}
        self.format = config['plateform']['cashapp']['format']
        # cashapp usernames are not case sensitive
        self.permutations_list = [perm.lower() for perm in permutations_list]
        # money
        self.type = config['plateform']['cashapp']['type']

    # Generate all potential cashapp usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        cashapp_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username, timeout=5)
            except requests.ConnectionError:
                print("failed to connect to cashapp")
            
            # If the account exists
            if r.status_code == 200:
                cashapp_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return cashapp_usernames