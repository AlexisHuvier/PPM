import os

class GitManager:
    def __init__(self):
        if not os.path.exists(".git"):
            os.system("git init")
    
    def init(self):
        os.system("git init")
    
    def status(self):
        status = os.popen("git status", "r").read()
        print(status)