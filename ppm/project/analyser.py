import os

class Analyser:
    def __init__(self, project):
        self.project = project
    
    def run_stats(self):
        files = []
        for dossier, sous_dossiers, fichiers in os.walk('.'):
            for fichier in fichiers:
                file = os.path.join(dossier, fichier)
                if ".git" not in file and ".ppm" not in file:
                    files.append(file)
        linespy = 0
        lines = 0
        for i in files:
            with open(i, 'r') as f:
                nb = len(f.readlines())
                lines += nb
                if ".py" in i:
                    linespy += nb
        stats = [
            "Fichiers :",
            *["  -> "+i+" ("+str(round(os.stat(i).st_size/1000, 2))+"ko)" for i in files],
            "Nombre de fichiers Python : " + str(len([i for i in files if ".py" in i])),
            "Nombre de fichiers totaux : " + str(len(files)),
            "Nombre de lignes de code Python : " + str(linespy),
            "Nombre de lignes totales : "+str(lines)
        ]
        return "\n".join(stats)