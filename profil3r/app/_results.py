from profil3r.app.colors import Colors


# Sanitize and format data obtained from scrapping
def format(result):
    if isinstance(result, list):
        return str(len(result)) + " results"
    elif result is None:
        return None
    else:
        result = result.replace('\n', ' ').strip()
        if result == "":
            return None
        else:
            return result

def print_results(self, element):
    if element in self.result:
        element_results = self.result[element]
        
        # Section title

        # No results
        if not element_results["accounts"]:
            print("\n" + Colors.OKGREEN + "{} ".format(element.upper()) + Colors.ENDC + Colors.FAIL + "× (No results)" + Colors.ENDC)
            return 
        # Results
        else: 
            print("\n" + Colors.OKGREEN + "{} ✓".format(element.upper()) + Colors.ENDC)

        # General case
        if element != "email":
            
            # Data scraped on the websites
            for account in element_results["accounts"]:
                print("➜ " + Colors.OKCYAN + account["value"] + Colors.ENDC)

                # print scraped element(s) (except value that was already printed)
                for index, element in list(account.items())[1:]:
                    element_value = format(element["value"])
                
                    if element_value is not None:
                        print("├── " + Colors.ENDC + Colors.BOLD + element["name"] + " : "  + Colors.ENDC + element_value)
        # Emails case
        else:
            possible_emails_list = [account["value"] for account in element_results["accounts"]]
            
            for account in element_results["accounts"]:
                # We pad the emails with spaces for better visibility
                longest_email_length = len(max(possible_emails_list))
                email = account["value"].ljust(longest_email_length + 7)

                # Breached account
                if account["breached"]:
                    print("➜ " + email + Colors.FAIL + "[BREACHED]" + Colors.ENDC)
                # Safe account
                else:
                    print("➜ " + email + Colors.OKGREEN + "[SAFE]" + Colors.ENDC)