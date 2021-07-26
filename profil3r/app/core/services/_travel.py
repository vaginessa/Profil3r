from profil3r.app.modules.travel.tripadvisor import Tripadvisor

# TripAdvisor
def tripadvisor(self):
    self.result["tripadvisor"] = Tripadvisor(self.config, self.permutations_list).search()
    # print results
    self.print_results("tripadvisor")
    return self.result["tripadvisor"]