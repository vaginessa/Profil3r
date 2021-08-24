from profil3r.app.colors import Colors

def print_logo(self):
    print(Colors.OKGREEN + Colors.BOLD + '''
    ____             _____ _______     
   / __ \_________  / __(_) /__  /_____
  / /_/ / ___/ __ \/ /_/ / / /_ </ ___/
 / ____/ /  / /_/ / __/ / /___/ / /    
/_/   /_/   \____/_/ /_/_//____/_/     
                                       
''' + Colors.ENDC)

    print(Colors.HEADER + "Version {version} - Developped by Rog3rSm1th\n".format(version=self.version) + Colors.ENDC)