from profil3r.app import Core
import os 

def main():
    CONFIG = '{}/config/config.json'.format(os.path.dirname(os.path.realpath(__file__)))
    profil3r = Core(CONFIG).run()