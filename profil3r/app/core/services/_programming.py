from profil3r.app.modules.programming.github import Github
from profil3r.app.modules.programming.pastebin import Pastebin
from profil3r.app.modules.programming.replit import Replit
from profil3r.app.modules.programming.pypi import PyPi
from profil3r.app.modules.programming.npm import Npm
from profil3r.app.modules.programming.asciinema import Asciinema
from profil3r.app.modules.programming.codementor import Codementor

# Github
def github(self):
    self.result["github"] = Github(self.config, self.permutations_list).search()
    # print results
    self.print_results("github")
    return self.result["github"]

# Pastebin
def pastebin(self):
    self.result["pastebin"] = Pastebin(self.config, self.permutations_list).search() 
    # print results
    self.print_results("pastebin")
    return self.result["pastebin"]

# Repl.it
def replit(self):
    self.result["replit"] = Replit(self.config, self.permutations_list).search() 
    # print results
    self.print_results("replit")
    return self.result["replit"]

# PyPi
def pypi(self):
    self.result["pypi"] = PyPi(self.config, self.permutations_list).search() 
    # print results
    self.print_results("pypi")
    return self.result["pypi"]

# Npm
def npm(self):
    self.result["npm"] = Npm(self.config, self.permutations_list).search() 
    # print results
    self.print_results("npm")
    return self.result["npm"]

# Asciinema
def asciinema(self):
    self.result["asciinema"] = Asciinema(self.config, self.permutations_list).search() 
    # print results
    self.print_results("asciinema")
    return self.result["asciinema"]

# Codementor
def codementor(self):
    self.result["codementor"] = Codementor(self.config, self.permutations_list).search() 
    # print results
    self.print_results("codementor")
    return self.result["codementor"]