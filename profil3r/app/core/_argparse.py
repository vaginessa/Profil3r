import argparse

# Usage :  profil3r.py [-h] -p PROFILE [PROFILE ...]
# Parse arguments from the command line using argparse
def parse_arguments(self):
    parser = argparse.ArgumentParser(description='Profil3r is an OSINT tool that allows you to find the differents social accounts, domains and emails used by a person')
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--profile', required=True, nargs='+', help="parts of the username that you are looking for, e.g. : john doe")
    parser.add_argument('-r', '--report', required=False, help="path to the report directory, e.g. : ./OSINT")
    args = parser.parse_args()
    
    # Items passed from the command line
    self.items = args.profile
    # Report path passed from the command line
    self.report_path = args.report.rstrip('/') if args.report is not None else args.report