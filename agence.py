from voiture import Voiture
from datetime import datetime


class Agence:
    def __init__(self):
        self.liste_voitures = []

    def rechercher_voiture(self, matricule):
        for voiture in self.liste_voitures:
            if voiture.matricule == matricule:
                return print("Voiture trouvé")
        return print("Voiture n'existe pas")

    def ajouter_voiture(self, voiture):
        if self.rechercher_voiture(voiture.matricule):
            raise ValueError(
                f"La voiture avec le matricule {voiture.matricule} existe déjà.")
        else:
            self.liste_voitures.append(voiture)

    def afficher_liste_voitures(self):
        if not self.liste_voitures:
            print("Il n'y a pas de voitures à afficher.")
            return
        for voiture in self.liste_voitures:
            voiture.afficher_voiture()

    def supprimer_voiture(self, matricule):
        for i, v in enumerate(self.liste_voitures):
            if v.matricule == matricule:
                del self.liste_voitures[i]
                return print("voiture supprimé")
        return print("voiture n'existe pas")


if __name__ == "__main__":
    voiture1 = Voiture("TN-123456", "Toyota", datetime(2022, 1, 1), 150000, 4)
    voiture2 = Voiture("TN-1234-AA", "Toyota", datetime(2015, 1, 1), 0, 3)
    voiture2 = Voiture("TN-998999", "BMW", datetime(2014, 1, 1), 0, 3)
agence = Agence()
agence.ajouter_voiture(voiture1)
agence.ajouter_voiture(voiture2)
agence.afficher_liste_voitures()
agence.rechercher_voiture("TN156")
agence.supprimer_voiture("TN-1234-AA")
agence.afficher_liste_voitures()
