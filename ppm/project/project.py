import os
import json

from project.gitmanager import GitManager

class Project:
    def __init__(self, directory, config):
        self.config = config
        self.directory = directory
        os.chdir(self.directory)
        self.ppm_directory = os.path.join(directory, ".ppm")
        self.python_directory = None
        self.project_file = os.path.join(directory, ".ppm", "project.json")
        if os.path.exists(".git"):
            self.git = GitManager()
        else:
            self.git = None
        if os.path.exists(self.project_file):
            with open(self.project_file, "r") as f:
                self.project_info = json.load(f)
            self.python_directory = os.path.join(directory, self.project_info["name"])
        else:
            self.project_info = self.create()
            self.save()
    
    def save(self):
        with open(self.project_file, "w") as f:
            json.dump(self.project_info, f, indent=4)

    def __str__(self):
        text = ["Directory : " + self.directory]
        for k, v in self.project_info.items():
            text.append(k.capitalize() + " : " + v)
        return "\n".join(text)

    def create(self):
        name = input("Project Name : ")
        author = input("Author : ")
        email = input("Email : ")
        description = input("Description : ")
        self.python_directory = os.path.join(self.directory, name.lower())
        os.makedirs(self.python_directory)
        if self.config.get("git", False):
            self.git = GitManager()
        with open(os.path.join(self.directory, "README.md"), "w") as f:
            f.write("# "+name+"\n\n"+description+"\n")
        with open(os.path.join(self.python_directory, "__init__.py"), "w") as f:
            f.write("__version__ = \"1.0.0\"")
        with open(os.path.join(self.directory, "setup.py"), "w") as f:
            f.write("""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages

import {namelower}

setup(

    name='{name}',

    version={namelower}.__version__,

    packages=find_packages(),
    author="{author}",
    author_email="{email}",
    description="{description}",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    include_package_data=True,

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning"
    ],
    install_requires=[]

 
)""".format(name=name, namelower=name.lower(), author=author, email=email, description=description))

        return { "name": name, "author": author, "email": email, "description": description }