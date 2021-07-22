from profil3r.app.modules.ctf.rootme import RootMe

# Root-Me
def rootme(self):
    self.result["rootme"] = RootMe(self.config, self.permutations_list).search()
    # print results
    self.print_results("rootme")