from profil3r.app.search import search_get
import time

class Dailymotion:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['dailymotion']['rate_limit'] / 1000
        # https://dailymotion.com/{username}
        self.format = config['plateform']['dailymotion']['format']
        self.permutations_list = permutations_list
        # Entertainment
        self.type = config['plateform']['dailymotion']['type']

    # Generate all potential dailymotion usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        dailymotion_usernames = {
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
                dailymotion_usernames["accounts"].append({"value": username})
            time.sleep(self.delay)
        
        return dailymotion_usernames