from profil3r.app.colors import Colors
import threading

def run(self):
    # Get arguments from the command line
    self.parse_arguments()
    
    self.load_config()
    self.print_logo()

    # Select modules from command line argument
    if self.cli_modules:
        self.modules_update(self.cli_modules)
    # Select modules from menu
    else:
        self.menu()

    modules = self.get_report_modules()

    self.get_permutations()

    # Keep only the most plausibles permutations if there are too many
    if len(self.permutations_list) >= 12:
        # If the user has passed the --filter argument
        if self.filter_results:
            self.filter()
        # Ask user to filter permutations
        else:
            while True:
                filter_choice = input("\nThere are a lot of permutation ({}), do you want to keep only the most plausibles ones ? (".format(len(self.permutations_list)) + Colors.OKGREEN + "Y" + Colors.ENDC + "/" + Colors.FAIL + "n" + Colors.ENDC + ")")
                if filter_choice.lower() == "y":
                    self.filter()
                    break
                if filter_choice.lower() == "n":
                    break

    if modules:
        # Number of permutations to test per service
        print("{} permutations to test for each service".format(len(self.permutations_list)))

        # List of services that profil3r will search
        print("\n" + "Profil3r will search : \n ➜ {} \n".format(str("\n ➜ ").join(modules)))

        for module in modules:
            thread = threading.Thread(target=self.modules[module]["method"])
            thread.start()
            thread.join()
    else:
        print("\nNo service selected.")
        
    if self.report_path:
        self.generate_report()