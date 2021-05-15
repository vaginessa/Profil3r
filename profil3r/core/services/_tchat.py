from profil3r.modules.tchat.skype import Skype

# Skype
def skype(self, verbose=True):
    self.result["skype"] = Skype(self.CONFIG, self.permutations_list).search() 
    # print results
    if verbose: self.print_results("skype")