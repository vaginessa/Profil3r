from profil3r.modules.porn.pornhub import Pornhub
from profil3r.modules.porn.redtube import Redtube
from profil3r.modules.porn.xvideos import XVideos

# Pornhub
def pornhub(self, verbose=True):
    self.result["pornhub"] = Pornhub(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("pornhub")

# Redtube
def redtube(self, verbose=True):
    self.result["redtube"] = Redtube(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("redtube")

# XVideos
def xvideos(self, verbose=True):
    self.result["xvideos"] = XVideos(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("xvideos")