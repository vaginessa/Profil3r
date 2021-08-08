from profil3r.app.search import search_get
import time

class Dota2:
    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['dota2']['rate_limit'] / 1000
        # https://api.opendota.com/api/search?q={permutation}
        self.format = config['plateform']['dota2']['format']
        # Opendota usernames are not case sensitive
        self.permutations_list = permutations_list
        # Gaming
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
        # URL of a Dota2 profile
        user_dota_url="https://www.opendota.com/players/{}"

        for username in possible_usernames_list:
            r = search_get(username)
            if not r:
                continue

            if r.status_code == 200:

                for user_dota in r.json():

                    # Append the account to the accounts table
                    opendota_usernames["accounts"].append({
                        "value": user_dota_url.format(str(user_dota ["account_id"])),
                        "user_username": {"name": "Name", "value": user_dota ["personaname"]},
                        "user_last_connection": {"name": "Last Connection", "value": user_dota ["last_match_time"] if "last_match_time" in user_dota else None},
                    })

            time.sleep(self.delay)   

        return  opendota_usernames 