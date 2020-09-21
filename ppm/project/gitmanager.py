import os

class GitManager:
    def __init__(self):
        if not os.path.exists(".git"):
            os.system("git init")
    
    def init(self):
        os.system("git init")
    
    def status(self):
        os.system("git status")
    
    def add(self, file):
        os.system("git add "+file)
        print("Added file in staging area done.")

    def branch(self, branch=None):
        if branch is None:
            os.system("git branch")
        else:
            branches = os.popen("git branch", "r").read()
            for i in branches.split("\n"):
                if i.replace("*", "").strip() == branch:
                    os.system("git switch "+branch)
                    return
            os.system("git switch -c "+branch)
    
    def commit(self, message):
        os.system("git commit -m \""+message+"\"")