import requests
from bs4 import BeautifulSoup
import time
import re

class Rootme:

    def __init__(self, config, permutations_list):
        # 1000 ms
        self.delay = config['plateform']['rootme']['rate_limit'] / 1000
        # https://www.rootme.org/{username}
        self.format = config['plateform']['rootme']['format']
        self.permutations_list = permutations_list
        # CTF
        self.type = config['plateform']['rootme']['type']

    # Generate all potential root-me usernames
    def possible_usernames(self):
        possible_usernames = []

        for permutation in self.permutations_list:
            possible_usernames.append(self.format.format(
                permutation = permutation,
            ))
        return possible_usernames

    def search(self):
        rootme_usernames = {
            "type": self.type,
            "accounts": []
        }
        possible_usernames_list = self.possible_usernames()

        for username in possible_usernames_list:
            try:
                r = requests.get(username, timeout=5)
            except requests.ConnectionError:
                print("failed to connect to rootme")
            
            # If the account exists
            if r.status_code == 200:
                # Account object
                account = {}

                # Get the username
                account["value"] = username
                
                # Parse HTML response content with beautiful soup 
                soup = BeautifulSoup(r.text, 'html.parser')
                
                # Scrape the user informations
                try:
                    user_rank = str(soup.find_all('h3')[4].get_text()).strip() if soup.find_all('h3') else None
                    user_score = str(soup.find_all('h3')[5].get_text()).strip() if soup.find_all('h3') else None
                    user_challenges_count = str(soup.find_all('h3')[6].get_text()).strip() if soup.find_all('h3') else None
                    user_machines_count = str(soup.find_all('h3')[7].get_text()).strip() if soup.find_all('h3') else None
                    user_website = str(soup.find_all('a', class_=re.compile('auteur-nom_site-*'))[0]['href']).strip() if soup.find_all('a', class_=re.compile('auteur-nom_site-*')) else None
                    user_bio = str(soup.find('li', class_=re.compile('auteur-bio-*')).find('p').get_text().replace("\n", " ")).strip() if soup.find('li', class_=re.compile('auteur-bio-*')) else None
                   
                    account["rank"] = {"name": "Rank", "value": user_rank}
                    account["score"] = {"name": "Score", "value": user_score}
                    account["challenges"] = {"name": "Challenges", "value": user_challenges_count}
                    account["machines"] = {"name": "Machines", "value": user_machines_count}
                    account["website"] = {"name": "Website", "value": user_website}
                    account["bio"] = {"name": "Bio", "value": user_bio}
                except:
                    pass
                
                # Append the account to the accounts table
                rootme_usernames["accounts"].append(account)

            time.sleep(self.delay)
        
        return rootme_usernames