#Script d'automatisation : trier et déplacer des fichiers dans de nouveaux fichiers créés

import os

chemin = r"C:\Users\mrgue\OneDrive\Desktop\Test\apprendrePython\là"

liste = os.listdir(chemin)
#print(liste)

for i in liste:

    images = "Fichiers_images"
    video = "Fichiers_vidéo"
    html = "Fichiers_html"
    py = "Fichiers_py"
    zip = "Fichiers_zip"
    nom, extension = os.path.splitext(i)
    if ".JPG" in extension or ".png" in extension:
        jonction = os.path.join(chemin, images)
        creation = os.makedirs(jonction, exist_ok=True)
        ancien_chemin = os.path.join(chemin, i)
        nouveau_chemin = os.path.join(jonction, i)
        deplacement = os.rename(ancien_chemin, nouveau_chemin)
        print(f"Fichier {i} déplacé vers /{images}")

    elif ".mp4" in extension:
        jonction2 = os.path.join(chemin, video)
        creation2 = os.makedirs(jonction2, exist_ok=True)
        ancien_chemin1 = os.path.join(chemin, i)
        nouveau_chemin1 = os.path.join(jonction2, i)
        deplacement2 = os.rename(ancien_chemin1, nouveau_chemin1)
        print(f"Fichier {i} déplacé vers /{video}")

    elif "html" in extension:
        jonction3 = os.path.join(chemin, html)
        creation3 = os.makedirs(jonction3, exist_ok=True)
        ancien_chemin3 = os.path.join(chemin, i)
        nouveau_chemin3 = os.path.join(jonction3, i)
        deplacement3 = os.rename(ancien_chemin3, nouveau_chemin3)
        print(f"Fichier {i} déplacé vers /{html}")

    elif "py" in extension:
        jonction4 = os.path.join(chemin, py)
        creation4 = os.makedirs(jonction4, exist_ok=True)
        ancien_chemin4 = os.path.join(chemin, i)
        nouveau_chemin4 = os.path.join(jonction4, i)
        deplacement4 = os.rename(ancien_chemin4, nouveau_chemin4)
        print(f"Fichier {i} déplacé vers /{py}")