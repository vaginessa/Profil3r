from profil3r.modules.hosting.aboutme import AboutMe
from profil3r.modules.hosting.wordpress import WordPress

# AboutMe
def aboutme(self):
    self.result["aboutme"] = AboutMe(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("aboutme")

# WordPress
def wordpress(self):
    self.result["wordpress"] = WordPress(self.CONFIG, self.permutations_list).search() 
    # print results
    self.print_results("wordpress")