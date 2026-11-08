import csv
from collections import Counter

FICHIER_ASSOCIATIONS = "data/associations.csv"
FICHIER_MATERIEL = "data/materiel.csv"
FICHIER_RESERVATIONS = "data/reservations.csv"
FICHIER_SITES = "data/sites.csv"

# Lire un fichier CSV et retourner une liste de dictionnaires dont chaque ligne représente une ligne du fichier.
def lire_csv(chemin : str) -> list[dict]:
    with open(chemin, encoding="utf-8", newline="") as fichier:
        lecteur = csv.DictReader(fichier)    
        return list(lecteur)   

# A partir d'une liste de dictionnaires, représentant les lignes d'un fichier CSV, et d'une colonne de ce fichier,
# compter les occurrences des valeur dans cette colonne.
def compter_par(lignes : list[dict], colonne : str) -> dict:
    compteur = Counter(ligne[colonne] for ligne in lignes)
    return dict(compteur)

# A partir d'une liste de dictionnaires, représentant les lignes d'un fichier CSV, et de deux colonnes de ce fichier,
# calculer la somme des valeurs de colonne_valeur pour chaque valeur distinctes de colonne_groupe.
def total_par(lignes : list[dict], colonne_groupe : str , colonne_valeur : str) -> dict:
    quantite_reservee = {}
    for ligne in lignes:
        groupe = ligne[colonne_groupe]
        valeur = int(ligne[colonne_valeur])
        if groupe in quantite_reservee:
            quantite_reservee[groupe] += valeur
        else:
            quantite_reservee[groupe] = valeur
    return quantite_reservee

#  Créer un objet de type Site
class Site:
    def __init__(self, code_site, nom, commune, annee_ouverture, surface_m2):
        self.code_site = code_site
        self.nom = nom
        self.commune = commune
        self.annee_ouverture = int(annee_ouverture)
        self.surface_m2 = int(surface_m2)

    def anciennete(self, annee_reference : int) -> int:
        return annee_reference - self.annee_ouverture

    def __str__(self) -> str:
        return (
            f"{self.code_site} — {self.nom} "
            f"({self.commune}), {self.surface_m2} m2"
        )
    
# A partir d'une liste de dictionnaires représentant les lignes du fichier "reservations.csv",
# retourner une liste de réservations dont le champ 'date_retour_reelle' est vide.
def reservations_en_cours(reservations : list[dict]) -> list:
    list_reservation = []
    for reservation in reservations:
        if reservation["date_retour_reelle"].strip() == "":
            list_reservation.append(reservation)
    return list_reservation


def main():
    # Verification lire_csv(chemin)
    sites = lire_csv(FICHIER_SITES)
    print(f"Nombre de lignes du fichier sites.csv : {len(sites)}")

    materiel = lire_csv(FICHIER_MATERIEL)
    print(f"Nombre de lignes du fichier matériel.csv : {len(materiel)}")

    associations = lire_csv(FICHIER_ASSOCIATIONS)
    print(f"Nombre de lignes du fichier associations.csv : {len(associations)}")

    reservations = lire_csv(FICHIER_RESERVATIONS)
    print(f"Nombre de lignes du fichier reservations : {len(reservations)}")

    # Verification class Site:
    site_Hazebrouck = Site("POL-HAZ", "Pole technique d'Hazebrouck", "Hazebrouck", 2009, 1800)
    print(f"Site de Hazebrouck : {site_Hazebrouck}, anciennete : {site_Hazebrouck.anciennete(2026)} ans")

    site_Bailleul = Site("POL-BAI", "Atelier municipal de Bailleul", "Bailleul", 1996, 950)
    print(f"Site de Bailleul : {site_Bailleul}, anciennete : {site_Bailleul.anciennete(2026)} ans")

    site_Merville = Site("POL-MER", "Depot intercommunal de Merville", "Merville", 2014, 1200)
    print(f"Site de Merville : {site_Merville}, anciennete : {site_Merville.anciennete(2026)} ans")

    site_Estaires = Site("POL-EST", "Reserve d'Estaires", "Estaires", 2001, 600)
    print(f"Site de Estaires : {site_Estaires}, anciennete : {site_Estaires.anciennete(2026)} ans")

    site_Nieppe = Site("POL-NIE", "Magasin de Nieppe", "Nieppe", 2018, 450)
    print(f"Site de Nieppe : {site_Nieppe}, anciennete : {site_Nieppe.anciennete(2026)} ans")

    # Verification compter_par(lignes, colonne) avec le fichier reservations.csv
    reservations = lire_csv(FICHIER_RESERVATIONS)
    compteur_reservations = compter_par(reservations, "code_site")
    print(f"Le nombre de réservations par code site est : {Counter.most_common(compteur_reservations)}")

    # Verification total_par(lignes, colonne_groupe, colonne_valeur)
    quantite_reservee_par_site = total_par(reservations, "code_site", "quantite")
    print(f"La quantité totale réservée par code_site est : {Counter.most_common(quantite_reservee_par_site)}")

    # Verification compter_par(lignes, colonne) avec le fichier materiel.csv
    # materiel = lire_csv(FICHIER_MATERIEL)
    compteur_materiel = compter_par(materiel, "etat")
    print(f"Le nombre de matériel par état est : {Counter.most_common(compteur_materiel)}")

    compteur_categorie = compter_par(materiel, "categorie")
    print(f"Le nombre de valeurs distinces de catégorie dans le fichier matériel.csv est : {len(compteur_categorie)}")

    # verification reservations_en_cours(reservations)
    liste_reservations_en_cours = reservations_en_cours(reservations)
    print(f"Les réservations en cours sont au nombre de : {len(liste_reservations_en_cours)}")


if __name__ == "__main__":    
    main()

