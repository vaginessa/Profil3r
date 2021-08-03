from profil3r.app.modules.hosting.aboutme import Aboutme
from profil3r.app.modules.hosting.wordpress import Wordpress
from profil3r.app.modules.hosting.slideshare import Slideshare

# AboutMe
def aboutme(self):
    self.result["aboutme"] = Aboutme(self.config, self.permutations_list).search() 
    # print results
    self.print_results("aboutme")
    return self.result["aboutme"]

# WordPress
def wordpress(self):
    self.result["wordpress"] = Wordpress(self.config, self.permutations_list).search() 
    # print results
    self.print_results("wordpress")
    return self.result["wordpress"]

# SlideShare
def slideshare(self):
    self.result["slideshare"] = Slideshare(self.config, self.permutations_list).search() 
    # print results
    self.print_results("slideshare")
    return self.result["slideshare"]