class Project:
    def __init__(self, directory):
        self.directory = directory

    def __str__(self):
        return "Project[ dir = {}]".format(self.directory)