from profil3r.app.modules.collaborative.wikipedia import Wikipedia
from profil3r.app.modules.collaborative.instructables import Instructables

# Wikipedia
def wikipedia(self):
    self.result["wikipedia"] = Wikipedia(self.config, self.permutations_list).search()
    # print results
    self.print_results("wikipedia")
    return self.result["wikipedia"]

# Instructables
def instructables(self):
    self.result["instructables"] = Instructables(self.config, self.permutations_list).search()
    # print results
    self.print_results("instructables")
    return self.result["instructables"]