#Petit script d'automatisation qui trie des images et déplace les anciennes images dans un fichier "Archives"

def script():
    from ntpath import isfile
    import os
    import time

    chemin =  r'C:\Users\mrgue\OneDrive\Desktop\Test\apprendrePython\images'

    temps = time.time()

    images = os.listdir(chemin)
    Sauvegarde_Archive = "Nouveau dossier de sauvegarde des archives"

    for image in images :
        print("="*30, "\n", image)
        chemin_complet = os.path.join(chemin, image)
        date_modif = os.path.getmtime(chemin_complet)
        dernier_temp = temps - date_modif
        
        if os.path.isfile(chemin_complet) and dernier_temp > 100 :
            chemin_sauvegarde = os.path.join(chemin, Sauvegarde_Archive)
            os.makedirs(chemin_sauvegarde, exist_ok=True)
            nouveau_chemin = os.path.join(chemin_sauvegarde, image)
            os.rename(chemin_complet, nouveau_chemin)
            print(f"Le fichier {image} a bien été ajouté au dossier {Sauvegarde_Archive}")
        
        print(dernier_temp)

script()