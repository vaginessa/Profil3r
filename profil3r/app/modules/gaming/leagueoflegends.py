import requests
from bs4 import BeautifulSoup
import time


class Leagueoflegends:
    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['leagueoflegends']['rate_limit'] / 1000
        # op.gg/summoner/userName={permutation}
        self.format = config['plateform']['leagueoflegends']['format']
        # league of legends usernames are not case sensitive
        self.permutations_list = permutations_list
        # gaming
        self.type = config['plateform']['leagueoflegends']['type']
        # servers
        self.servers = config['plateform']['leagueoflegends']['servers']

    # Generate all potential league of legends usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation=permutation,
            ))
        return possible_usernames

    def search(self):
        leagueoflegends_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()
        for username in possible_usernames_list:
            for serve in self.servers:
                # {https://lan}{.op.gg/summoner/userName=name12}
                url = serve["url"].format(username)
                try:
                    r = requests.get(url, timeout=5)
                except requests.ConnectionError:
                    print("failed to connect to op gg")
                    pass
                if r.ok:
                    account = {}
                    account["value"] = url
                    soup = BeautifulSoup(r.text, 'html.parser')
                    try:
                        name = str(soup.find_all(class_="Name")[0].get_text()) if soup.find_all(
                            class_="Name") else None
                        elo = str(soup.find_all(class_="TierRank")[0].get_text()) if soup.find_all(
                            class_="TierRank") else None
                        last_connection = str(soup.find_all(class_="TimeStamp")[0].find_all(
                            class_="_timeago")[0].get_text()) if soup.find_all(class_="TimeStamp") else None
                        # IF the account exists
                        if name:
                            account["name"] = {"name": "Name", "value": name}
                            account["location"] = {
                                "name": "Location", "value": serve["name"]}
                            account["last_connection"] = {
                                "name": "Last Connection", "value": last_connection}
                            account["elo"] = {"name": "Elo", "value": elo}
                            leagueoflegends_usernames["accounts"].append(
                                account)
                    except:
                        pass
                time.sleep(self.delay)
        return leagueoflegends_usernames
