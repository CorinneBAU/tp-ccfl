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


def main():
    sites = lire_csv(FICHIER_SITES)
    print(f"Nombre de sites : {len(sites)}")

if __name__ == "__main__":    
    main()

