import pandas as pd


FICHIER_ASSOCIATIONS = "data/associations.csv"
FICHIER_MATERIEL = "data/materiel.csv"
FICHIER_RESERVATIONS = "data/reservations.csv"
FICHIER_SITES = "data/sites.csv" 

# Charger les fichiers CSV dans des DataFrames Pandas et convertir les colonnes de dates 
# date_debut, date_fin_prevue et date_retour_reelle en dates (format datetime).
df_sites = pd.read_csv(FICHIER_SITES)
df_materiel = pd.read_csv(FICHIER_MATERIEL)
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


print("Quelques informations sur le DataFrame 'reservations' :")
print("shape")
print(df_reservations.shape)
print("info")
print(df_reservations.info())
print("valeurs manquantes")
print(df_reservations.isna().sum())