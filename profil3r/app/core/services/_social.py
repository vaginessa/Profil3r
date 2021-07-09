from profil3r.app.modules.social.facebook import Facebook
from profil3r.app.modules.social.twitter import Twitter
from profil3r.app.modules.social.tiktok import TikTok
from profil3r.app.modules.social.instagram import Instagram
from profil3r.app.modules.social.pinterest import Pinterest
from profil3r.app.modules.social.linktree import LinkTree
from profil3r.app.modules.social.myspace import MySpace
from profil3r.app.modules.social.flickr import Flickr
from profil3r.app.modules.social.goodread import GoodRead

# Facebook
def facebook(self):
    self.result["facebook"] = Facebook(self.config, self.permutations_list).search()
    # print results
    self.print_results("facebook")

# Twitter
def twitter(self):
    self.result["twitter"] = Twitter(self.config, self.permutations_list).search()
    # print results
    self.print_results("twitter")

# TikTok
def tiktok(self):
    self.result["tiktok"] = TikTok(self.config, self.permutations_list).search()
    # print results
    self.print_results("tiktok")

# Instagram
def instagram(self):
    self.result["instagram"] = Instagram(self.config, self.permutations_list).search()
    # print results
    self.print_results("instagram")

# Pinterest
def pinterest(self):
    self.result["pinterest"] = Pinterest(self.config, self.permutations_list).search()
    # print results
    self.print_results("pinterest")

# LinkTree
def linktree(self):
    self.result["linktree"] = LinkTree(self.config, self.permutations_list).search()
    # print results
    self.print_results("linktree")

# MySpace
def myspace(self):
    self.result["myspace"] = MySpace(self.config, self.permutations_list).search()
    # print results
    self.print_results("myspace")

# Flickr
def flickr(self):
    self.result["flickr"] = Flickr(self.config, self.permutations_list).search()
    # print results
    self.print_results("flickr")

# GoodRead
def goodread(self):
    self.result["goodread"] = GoodRead(self.config, self.permutations_list).search()
    # print results
    self.print_results("goodread")