import os
import stat
import datetime

def lister_fichiers(repertoire='.'):
    try:
        fichiers = os.listdir(repertoire)
        for fichier in fichiers:
            chemin = os.path.join(repertoire, fichier)
            stat_info = os.stat(chemin)
            taille = stat_info.st_size
            date_modif = datetime.datetime.fromtimestamp(stat_info.st_mtime)

            # Afficher le nom du fichier, la taille et la date de modification
            print(f"{fichier}\tTaille: {taille} octets\tModifié le: {date_modif}")
    except OSError as e:
        print(f"Erreur: {e}")

# Utilisation de la fonction avec le répertoire courant
lister_fichiers()
