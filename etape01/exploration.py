import csv
from collections import Counter

FICHIER_ASSOCIATIONS = "data/associations.csv"
FICHIER_MATERIEL = "data/materiel.csv"
FICHIER_RESERVATIONS = "data/reservations.csv"
FICHIER_SITES = "data/sites.csv"

def lire_csv(chemin):
    with open(chemin, encoding="utf-8", newline="") as fichier:
        lecteur = csv.DictReader(fichier)
        return list(lecteur)   


def compter_par(lignes, colonne):
    compteur = Counter(ligne[colonne] for ligne in lignes)
    return dict(compteur)


def main():
    # Verification lire_csv(chemin)
    sites = lire_csv(FICHIER_SITES)
    print(f"Nombre de sites : {len(sites)}")

    materiel = lire_csv(FICHIER_MATERIEL)
    print(f"Nombre de matériels : {len(materiel)}")

    associations = lire_csv(FICHIER_ASSOCIATIONS)
    print(f"Nombre d'associations : {len(associations)}")

    reservations = lire_csv(FICHIER_RESERVATIONS)
    print(f"Nombre de réservations : {len(reservations)}")

    # Verification compter_par(lignes, colonne):
    materiel = lire_csv(FICHIER_MATERIEL)
    compteur_materiel = compter_par(materiel, "etat")
    print(compteur_materiel)

if __name__ == "__main__":    
    main()

