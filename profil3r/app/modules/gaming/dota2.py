import requests
import time

class Dota2:
    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['dota2']['rate_limit'] / 1000
        # https://api.opendota.com/api/search?q={permutation}
        self.format = config['plateform']['dota2']['format']
        # opendota usernames are not case sensitive
        self.permutations_list = permutations_list
        # gaming
        self.type = config['plateform']['dota2']['type']
    
    # Generate all potential opendota usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames
    def search(self):
        opendota_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()
        user_dota_url="https://www.opendota.com/players/{}"
        for username in possible_usernames_list:
            try:
                r = requests.get(username, timeout=5)
            except requests.ConnectionError:
                print("failed to connect to opendota")
            if r.ok:
                for userDota in r.json():
                    opendota_usernames["accounts"].append({
                        "value":user_dota_url.format(str(userDota["account_id"])),
                        "user_username":{"name": "Name", "value": userDota["personaname"]},
                        "user_last_connection":{"name": "Last Connection", "value": userDota["last_match_time"] if "last_match_time" in userDota else None},
                        "user_avatar":{"name": "Avatar", "value": userDota["avatarfull"]}
                    })
            time.sleep(self.delay)   
        return  opendota_usernames 