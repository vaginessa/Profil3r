from profil3r.app.modules.social.facebook import Facebook
from profil3r.app.modules.social.twitter import Twitter
from profil3r.app.modules.social.tiktok import Tiktok
from profil3r.app.modules.social.instagram import Instagram
from profil3r.app.modules.social.pinterest import Pinterest
from profil3r.app.modules.social.linktree import Linktree
from profil3r.app.modules.social.myspace import Myspace
from profil3r.app.modules.social.flickr import Flickr
from profil3r.app.modules.social.goodread import Goodread

# Facebook
def facebook(self):
    self.result["facebook"] = Facebook(self.config, self.permutations_list).search()
    # print results
    self.print_results("facebook")
    return self.result["facebook"]

# Twitter
def twitter(self):
    self.result["twitter"] = Twitter(self.config, self.permutations_list).search()
    # print results
    self.print_results("twitter")
    return self.result["twitter"]

# TikTok
def tiktok(self):
    self.result["tiktok"] = Tiktok(self.config, self.permutations_list).search()
    # print results
    self.print_results("tiktok")
    return self.result["tiktok"]

# Instagram
def instagram(self):
    self.result["instagram"] = Instagram(self.config, self.permutations_list).search()
    # print results
    self.print_results("instagram")
    return self.result["instagram"]

# Pinterest
def pinterest(self):
    self.result["pinterest"] = Pinterest(self.config, self.permutations_list).search()
    # print results
    self.print_results("pinterest")
    return self.result["pinterest"]

# LinkTree
def linktree(self):
    self.result["linktree"] = Linktree(self.config, self.permutations_list).search()
    # print results
    self.print_results("linktree")
    return self.result["linktree"]

# MySpace
def myspace(self):
    self.result["myspace"] = Myspace(self.config, self.permutations_list).search()
    # print results
    self.print_results("myspace")
    return self.result["myspace"]

# Flickr
def flickr(self):
    self.result["flickr"] = Flickr(self.config, self.permutations_list).search()
    # print results
    self.print_results("flickr")
    return self.result["flickr"]

# GoodRead
def goodread(self):
    self.result["goodread"] = Goodread(self.config, self.permutations_list).search()
    # print results
    self.print_results("goodread")
    return self.result["goodread"]