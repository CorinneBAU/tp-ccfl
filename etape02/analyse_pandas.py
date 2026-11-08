import pandas as pd


FICHIER_ASSOCIATIONS = "data/associations.csv"
FICHIER_MATERIEL = "data/materiel.csv"
FICHIER_RESERVATIONS = "data/reservations.csv"
FICHIER_SITES = "data/sites.csv" 

# Charger les fichiers CSV dans des DataFrames Pandas et convertir les colonnes de dates 
# date_debut, date_fin_prevue et date_retour_reelle en dates (format datetime).
df_sites = pd.read_csv(FICHIER_SITES)
df_materiel = pd.read_csv(FICHIER_MATERIEL,)
df_associations = pd.read_csv(FICHIER_ASSOCIATIONS)
df_reservations = pd.read_csv(FICHIER_RESERVATIONS,
                              parse_dates=["date_debut", "date_fin_prevue", "date_retour_reelle"])

print("Quelques informations sur le DataFrame 'materiel' :")
print("shape")
print(df_materiel.shape)
print("info")
print(df_materiel.info())
print("valeurs manquantes")
print(df_materiel.isna().sum())

# La valeur_achat est de type str car elle contient des cellules avec des guillements ("").
df_materiel["valeur_achat"] = df_materiel["valeur_achat"].str.replace(",", ".").astype(float)
print("info après conversion de la colonne 'valeur_achat' en float")
print(df_materiel.info())

# Trier le DataFrame df_materiel par la colonne valeur_achat de manière décroissante.
df_materiel.sort_values("valeur_achat", ascending=False)

# Afficher les 10 matériels les plus chers après le tri.
print(f"Les 10 matériels les plus chers :")
print(
    df_materiel[
        ["reference","designation","categorie","valeur_achat"]
        ].head(10))

# Afficher le nombre de matériels par catégorie (du + fréquent ou - fréquent)
print("Nombre de matériels par catégorie :")
nb_materiel_par_categorie = df_materiel["categorie"].value_counts()
print(nb_materiel_par_categorie)


print("Quelques informations sur le DataFrame 'reservations' :")
print("shape")
print(df_reservations.shape)
print("info")
print(df_reservations.info())
print("valeurs manquantes")
print(df_reservations.isna().sum())
print("Nombre de réservations et quantité totale par code_site :")
print(df_reservations.groupby("code_site")
      .agg(nb_reservation=("id_reservation", "size"), 
           quantite_empruntée=("quantite", "sum")).sort_values("nb_reservation", ascending=False)
        )