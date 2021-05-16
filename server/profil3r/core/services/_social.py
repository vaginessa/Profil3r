from profil3r.modules.social.facebook import Facebook
from profil3r.modules.social.twitter import Twitter
from profil3r.modules.social.tiktok import TikTok
from profil3r.modules.social.instagram import Instagram
from profil3r.modules.social.pinterest import Pinterest
from profil3r.modules.social.linktree import LinkTree
from profil3r.modules.social.myspace import MySpace

# Facebook
def facebook(self, verbose=True):
    self.result["facebook"] = Facebook(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("facebook")

# Twitter
def twitter(self, verbose=True):
    self.result["twitter"] = Twitter(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("twitter")

# TikTok
def tiktok(self, verbose=True):
    self.result["tiktok"] = TikTok(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("tiktok")

# Instagram
def instagram(self, verbose=True):
    self.result["instagram"] = Instagram(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("instagram")

# Pinterest
def pinterest(self, verbose=True):
    self.result["pinterest"] = Pinterest(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("pinterest")

# LinkTree
def linktree(self, verbose=True):
    self.result["linktree"] = LinkTree(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("linktree")

# MySpace
def myspace(self, verbose=True):
    self.result["myspace"] = MySpace(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("myspace")