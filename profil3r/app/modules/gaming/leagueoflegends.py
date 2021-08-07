from profil3r.app.search import search_get
from bs4 import BeautifulSoup
import time

class Leagueoflegends:
    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['leagueoflegends']['rate_limit'] / 1000
        # op.gg/summoner/userName={permutation}
        self.format = config['plateform']['leagueoflegends']['format']
        # League of legends usernames are not case sensitive
        self.permutations_list = permutations_list
        # Gaming
        self.type = config['plateform']['leagueoflegends']['type']
        # Servers
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
            for server in self.servers:
                # {subdomain}{username}
                url = server["url"].format(username)
                r = search_get(url)
                if not r:
                    continue

                if r.ok:
                    account = {}
                    account["value"] = url
                    soup = BeautifulSoup(r.text, 'html.parser')
                    try:
                        name = str(soup.find_all(class_="Name")[0].get_text()) if soup.find_all(class_="Name") else None
                        elo = str(soup.find_all(class_="TierRank")[0].get_text()) if soup.find_all(class_="TierRank") else None
                        last_connection = str(soup.find_all(class_="TimeStamp")[0].find_all(class_="_timeago")[0].get_text()) if soup.find_all(class_="TimeStamp") else None
                        # If the account exists
                        if name:
                            account["user_username"] = {"name": "Name", "value": name}
                            account["user_location"] = {"name": "Location", "value": server["name"]}
                            account["user_last_connection"] = {"name": "Last Connection", "value": last_connection}
                            account["user_elo"] = {"name": "Elo", "value": elo}
                            leagueoflegends_usernames["accounts"].append(account)
                    except:
                        pass
                time.sleep(self.delay)
                
        return leagueoflegends_usernames