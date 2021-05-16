from profil3r.modules.forum.zeroxzerozerosec import ZeroxZeroZeroSec
from profil3r.modules.forum.jeuxvideo import JeuxVideo
from profil3r.modules.forum.hackernews import Hackernews
from profil3r.modules.forum.crackedto import CrackedTo

# 0x00sec
def zeroxzerozerosec(self, verbose=True):
    self.result["0x00sec"] = ZeroxZeroZeroSec(self.CONFIG, self.permutations_list).search() 
    # print results
    if verbose: self.print_results("0x00sec")

# jeuxvideo.com
def jeuxvideo(self, verbose=True):
    self.result["jeuxvideo.com"] = JeuxVideo(self.CONFIG, self.permutations_list).search() 
    # print results
    if verbose: self.print_results("jeuxvideo.com")

# Hackernews
def hackernews(self, verbose=True):
    self.result["hackernews"] = Hackernews(self.CONFIG, self.permutations_list).search() 
    # print results
    if verbose: self.print_results("hackernews")

# Cracked.to
def crackedto(self, verbose=True):
    self.result["crackedto"] = CrackedTo(self.CONFIG, self.permutations_list).search() 
    # print results
    if verbose: self.print_results("crackedto")