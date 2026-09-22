# Petite classe qui prend en entrée un age à ajouter et l'affiche à l'utilisateur

class Human:
    def __init__(self, Homme, Femme, Enfant):
        self.Homme = Homme
        self.Femme = Femme
        self.Enfant = Enfant
        self.age = 0

    def grandir(self, ajout_age):
        self.age += ajout_age
    
    def afficher(self, infos):
        print(f"L'âge est égal à {self.age}")


Grand = Human("Madou", "Awa", "Ali")
Grand.grandir(2)
Grand.afficher("Affiche le résultat")


class Animal(Human):
    def __init__(self, homme, femme, enfant):
        super().__init__(homme, femme, enfant)
        self.taille = 0

    def elever(self, niveau):
        self.taille += niveau


niveauAnimal = Animal("Lion", "Lionne", "Lionceau")
niveauAnimal.elever(3)
print(niveauAnimal)