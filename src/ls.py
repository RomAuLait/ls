import os

def lister_fichiers(repertoire='.'):
    try:
        fichiers = os.listdir(repertoire)
        for fichier in fichiers:
            print(fichier)
    except OSError as e:
        print(f"Erreur: {e}")

# Utilisation de la fonction avec le répertoire courant
lister_fichiers()
