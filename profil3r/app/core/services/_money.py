from profil3r.app.modules.money.buymeacoffee import Buymeacoffee
from profil3r.app.modules.money.patreon import Patreon

# BuyMeACoffee
def buymeacoffee(self):
    self.result["buymeacoffee"] = Buymeacoffee(self.config, self.permutations_list).search() 
    # print results
    self.print_results("buymeacoffee")
    return self.result["buymeacoffee"]

# Patreon
def patreon(self):
    self.result["patreon"] = Patreon(self.config, self.permutations_list).search() 
    # print results
    self.print_results("patreon")
    return self.result["patreon"]