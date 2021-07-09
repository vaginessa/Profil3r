from app.modules.forum.zeroxzerozerosec import ZeroxZeroZeroSec
from app.modules.forum.jeuxvideo import JeuxVideo
from app.modules.forum.hackernews import Hackernews
from app.modules.forum.crackedto import CrackedTo
from app.modules.forum.lesswrong import LessWrong

# 0x00sec
def zeroxzerozerosec(self):
    self.result["0x00sec"] = ZeroxZeroZeroSec(self.config, self.permutations_list).search() 
    # print results
    self.print_results("0x00sec")

# jeuxvideo.com
def jeuxvideo(self):
    self.result["jeuxvideo.com"] = JeuxVideo(self.config, self.permutations_list).search() 
    # print results
    self.print_results("jeuxvideo.com")

# Hackernews
def hackernews(self):
    self.result["hackernews"] = Hackernews(self.config, self.permutations_list).search() 
    # print results
    self.print_results("hackernews")

# Cracked.to
def crackedto(self):
    self.result["crackedto"] = CrackedTo(self.config, self.permutations_list).search() 
    # print results
    self.print_results("crackedto")

# LessWrong
def lesswrong(self):
    self.result["lesswrong"] = LessWrong(self.config, self.permutations_list).search() 
    # print results
    self.print_results("lesswrong")