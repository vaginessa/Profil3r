from profil3r.app.modules.domain.domain import Domain

# Domain
def domain(self):
    self.result["domain"] = Domain(self.config, self.permutations_list).search()
    # print results
    self.print_results("domain")