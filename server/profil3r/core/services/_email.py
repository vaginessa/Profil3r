from profil3r.modules.email.email import Email

# Emails
def email(self, verbose=True):
    self.result["email"] = Email(self.CONFIG, self.permutations_list).search()
    # print results
    if verbose: self.print_results("email")