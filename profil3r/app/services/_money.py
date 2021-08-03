from profil3r.app.modules.money.buymeacoffee import Buymeacoffee
from profil3r.app.modules.money.patreon import Patreon
from profil3r.app.modules.money.cashapp import Cashapp

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

# CashApp
def cashapp(self):
    self.result["cashapp"] = Cashapp(self.config, self.permutations_list).search() 
    # print results
    self.print_results("cashapp")
    return self.result["cashapp"]