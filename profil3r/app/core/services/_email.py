from profil3r.app.modules.email.email import Email

# Emails
def email(self):
    self.result["email"] = Email(self.config, self.permutations_list).search()
    # print results
    self.print_results("email")