from profil3r.modules.domain.domain import Domain

# Domain
def domain(self, verbose=True):
    self.result["domain"] = Domain(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("domain")