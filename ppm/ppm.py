import sys
import os

from utils import Config
from project import Project

class PPM:
    def __init__(self):
        self.usages = {"Config": "ppm config <param> <value>", "Project Creation": "ppm create", "Help": "ppm help | ppm -h | ppm --help"}
        self.conf = Config()
        if os.path.exists(".ppm"):
            self.project = Project(os.getcwd())
        else:
            self.project = None
        
    def create_project(self):
        if self.project is None:
            os.makedirs(".ppm")
            self.project = Project(os.getcwd())
            print("Project Created")
        else:
            print("Error : You are in a project.")

    def usage(self, type_ = None):
        if type_ is None or type_ not in self.usages.keys():
            print("Commands :")
            for k, v in self.usages.items():
                print(" ->", k, ":", v)
        else:
            print("Usage : ", self.usages[type_])

    def show_config(self, key = None):
        if key is None or key not in self.conf.config.keys():
            print("Config :")
            for k, v in self.conf.config.items():
                print(" ->", k, ":", v)
        else:
            print(key, ":", self.conf.get(key, None))

    def run(self):
        if len(sys.argv) == 1:
            self.usage()
        elif len(sys.argv) == 2:
            if sys.argv[1] in ["help", "-h", "--help"]:
                self.usage()
            elif sys.argv[1] == "create":
                self.create_project()
            elif sys.argv[1] == "config":
                self.show_config()
            else:
                self.usage()
        elif len(sys.argv) == 3:
            if sys.argv[1] == "config":
                if sys.argv[2] in conf.config.keys():
                    self.show_config(sys.argv[2])
                else:
                    print("Config : Unknown value")
            else:
                self.usage() 
        elif len(sys.argv) == 4:
            if sys.argv[1] == "config":
                if sys.argv[2] == "git":
                    if sys.argv[3].lower() in ["true", "false"]:
                        self.conf.set(sys.argv[2], True if sys.argv[3].lower() == "true" else False)
                        self.conf.save()
                    else:
                        print("Config : Git take a boolean value")
                else:
                    print("Config : Unknown value")
            else:
                self.usage()
        else:
            self.usage()
            

if __name__ == "__main__":
    ppm = PPM()
    ppm.run()