from profil3r.app.modules.programming.github import Github
from profil3r.app.modules.programming.pastebin import Pastebin
from profil3r.app.modules.programming.replit import Replit
from profil3r.app.modules.programming.pypi import PyPi

# Github
def github(self):
    self.result["github"] = Github(self.config, self.permutations_list).search()
    # print results
    self.print_results("github")

# Pastebin
def pastebin(self):
    self.result["pastebin"] = Pastebin(self.config, self.permutations_list).search() 
    # print results
    self.print_results("pastebin")

# Repl.it
def replit(self):
    self.result["replit"] = Replit(self.config, self.permutations_list).search() 
    # print results
    self.print_results("replit")

# PyPi
def pypi(self):
    self.result["pypi"] = PyPi(self.config, self.permutations_list).search() 
    # print results
    self.print_results("pypi")