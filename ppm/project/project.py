import os
import json

class Project:
    def __init__(self, directory, config):
        self.config = config
        self.directory = directory
        self.project_file = os.path.join(directory, ".ppm", "project.json")
        if os.path.exists(self.project_file):
            with open(self.project_file, "r") as f:
                self.project_info = json.load(f)
        else:
            self.project_info = self.create()
            self.save()

    def create(self):
        name = input("Project Name : ")
        author = input("Author : ")
        if self.config.get("git", False):
            os.system("git init")
        return { "name": name, "author": author }
    
    def save(self):
        with open(self.project_file, "w") as f:
            json.dump(self.project_info, f, indent=4)

    def __str__(self):
        text = ["Directory : " + self.directory]
        for k, v in self.project_info.items():
            text.append(k.capitalize() + " : " + v)
        return "\n".join(text)