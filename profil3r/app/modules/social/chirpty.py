import requests
import time

class Chirpty:
    
    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['chirpty']['rate_limit'] / 1000
        # https://chirpty.com/api/circle?screen_name={permutation}
        self.format = config['plateform']['chirpty']['format']
        # chirpty usernames are not case sensitive
        self.permutations_list = permutations_list
        #social
        self.type = config['plateform']['chirpty']['type']

    # Generate all potential chirpty usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        chirpty_usernames = {
            "type": self.type,
            "accounts" : []
        }
        possible_usernames_list = self.possible_usernames()
        user_circle_twitter="https://twitter.com/{}"
        for username in possible_usernames_list:
            try:
                r=requests.get(username,timeout=5)
            except requests.ConnectionError:
                print("failed to connect to chirpty")  
            if r.ok:
                lvl=0
                try:
                    for circles in r.json()["data"]:
                        lvl+=1
                        for circle in circles:
                            chirpty_usernames["accounts"].append({
                                "value":user_circle_twitter.format(circle["screen_name"]),
                                "user_circle_lvl":{"name": "Circle", "value": str(lvl)},
                                "username": {"name": "Username", "value": circle["screen_name"]},
                                "user_id": {"name": "User id", "value": circle["id"]},
                                "total_interaction": {"name": "Total interaction", "value":str(circle["total"])} 
                            })                    
                except:
                    print("not found")
                    pass
            time.sleep(self.delay)
        return chirpty_usernames   