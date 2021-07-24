from profil3r.app.modules.medias.medium import Medium
from profil3r.app.modules.medias.devto import DevTo

# Medium
def medium(self):
    self.result["medium"] = Medium(self.config, self.permutations_list).search()
    # print results
    self.print_results("medium")
    return self.result["medium"]

# Dev.to
def devto(self):
    self.result["devto"] = DevTo(self.config, self.permutations_list).search()
    # print results
    self.print_results("devto")
    return self.result["devto"]