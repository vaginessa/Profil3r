from profil3r.app.modules.ctf.rootme import Rootme

# Root-Me
def rootme(self):
    self.result["rootme"] = Rootme(self.config, self.permutations_list).search()
    # print results
    self.print_results("rootme")
    return self.result["rootme"]