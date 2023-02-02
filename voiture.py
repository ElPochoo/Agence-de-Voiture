from datetime import datetime


class Voiture:
    def __init__(self, matricule="", marque="", date_circulation=datetime.now(), kilometrage="", cylindre=""):
        self.matricule = matricule
        self.marque = marque
        self.date_circulation = date_circulation
        self.kilometrage = kilometrage
        self.cylindre = cylindre

    def saisir_voiture(self):
        self.matricule = input("Entrez la matricule : ")
        self.marque = input("Entrez la marque : ")
        date_circulation = input(
            "Entrez la date de circulation (format YYYY-MM-DD) : ")
        date_circulation = datetime.strptime(date_circulation, "%Y-%m-%d")
        self.kilometrage = input("Entrez le kilométrage : ")
        self.cylindre = input("Entrez le cylindre : ")

    def afficher_voiture(self):
        print("Matricule : %s, Marque : %s, Date de circulation : %s, Kilométrage : %s, Cylindre : %s" % (
            self.matricule, self.marque, self.date_circulation.strftime("%d-%m-%Y"), self.kilometrage, self.cylindre))


if __name__ == "__main__":
    v = Voiture()
    v.saisir_voiture()
    v.afficher_voiture()
