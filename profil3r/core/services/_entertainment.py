from profil3r.modules.entertainment.dailymotion import Dailymotion
from profil3r.modules.entertainment.vimeo import Vimeo

# Dailymotion
def dailymotion(self, verbose=True):
    self.result["dailymotion"] = Dailymotion(self.CONFIG, self.permutations_list).search() 
    # print results
    if verbose: self.print_results("dailymotion")

# Vimeo
def vimeo(self, verbose=True):
    self.result["vimeo"] = Vimeo(self.CONFIG, self.permutations_list).search() 
    # print results
    if verbose: self.print_results("vimeo")