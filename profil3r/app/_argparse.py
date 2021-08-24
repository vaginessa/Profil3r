import argparse
import re

# Usage: profil3r [-h] -p PROFILE [PROFILE ...] [-r REPORT] [--services SERVICES [SERVICES ...]] [-f] [-s SEPARATORS [SEPARATORS ...]]
# Parse arguments from the command line using argparse
def parse_arguments(self):
    parser = argparse.ArgumentParser(description='Profil3r is an OSINT tool that allows you to find the differents social accounts, domains and emails used by a person')
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--profile', required=True, nargs='+', help="parts of the username that you are looking for. e.g. john doe")
    parser.add_argument('-r', '--report', required=False, help="path to the report directory. e.g. ./OSINT")
    parser.add_argument('--services', required=False, nargs='+', help="list of services to search, separated by a comma. e.g. facebook,twitter,email")
    parser.add_argument('-f', '--filter', required=False, action='store_true', help="filters the permutations by keeping only the most plausible ones")
    parser.add_argument('-s', '--separators', required=False, nargs='+', help="separators. e.g . - _")
    args = parser.parse_args()
    
    # Items passed from the command line
    self.items = args.profile
    # Report path passed from the command line
    self.report_path = args.report.rstrip('/') if args.report is not None else args.report
    # List of services to search
    self.cli_services = args.services
    # Filter permutations
    self.filter_results = args.filter
    # Separators passed from the command line
    self.separators = list(set(self.config['separators'].values()) & set(args.separators)) if args.separators is not None else None