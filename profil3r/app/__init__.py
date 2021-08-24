import os
from glob import glob
import re
from pathlib import Path

class Core(object):

    from ._menu import menu
    from ._permutations import get_permutations
    from ._results import print_results
    from ._run import run
    from ._report import generate_report, generate_json_report, generate_HTML_report, generate_csv_report
    from ._modules import modules_update, get_report_modules
    from ._logo import print_logo
    from ._argparse import parse_arguments
    from ._config import load_config
    from ._filter import filter

    def __init__(self, config_path):
        self.config_path = config_path
        self.version = "1.4.8" 
        self.separators = []
        self.result = {}
        self.permutations_list = []
        self.modules = {}

        # Automatic creation of a self.module object containing all methods related to scrapping
        # self.module = {
        #     "facebook": {"method": self.facebook},
        #     ...
        # }
        modules = modules = glob("{}/*/*".format(modules_dir, category))
        modules = list(filter(module_category_regexp.match, list(map(lambda x: Path(x).name, modules))))
        modules = [module[:-3] for module in modules]
        for module in modules:
            self.modules[module] = {"method": getattr(self, module)}

# Automatic creation of the methods used to scrape the different services
module_regexp = re.compile("[a-z0-9]+\.py")
module_category_regexp = re.compile("[a-z]+")

# Modules are in profil3r/app/modules/
current_dir = os.path.dirname(os.path.realpath(__file__))
modules_dir = "{}/modules/".format(current_dir)

# List of of the different categories : ["collaborative", "ctf", ...]
modules_categories = modules = glob("{}/*".format(modules_dir))
modules_categories = list(filter(module_category_regexp.match, list(map(lambda x: Path(x).name, modules))))

for category in modules_categories:
    # Get the list of all modules present in the /modules folder ["instructables", "wikipedia", ...]
    modules = modules = glob("{}/{}/*".format(modules_dir, category))
    modules = list(filter(module_category_regexp.match, list(map(lambda x: Path(x).name, modules))))
    # remove .py at the end of the module file name
    modules = [module[:-3] for module in modules]

    # For each module, we create a method of the Core class that will scrape the profile on the service
    # then display the result
    for module in modules:
        exec("""
from profil3r.app.modules.{category_name}.{module_name} import {module_name_capitalize}

def {module_name}(self):
    self.result["{module_name}"] = {module_name_capitalize}(self.config, self.permutations_list).search()
    # print results
    self.print_results("{module_name}")
    return self.result["{module_name}"]

setattr(Core, '{module_name}', {module_name})
        """.format(category_name=category, module_name=module, module_name_capitalize=module.capitalize()))