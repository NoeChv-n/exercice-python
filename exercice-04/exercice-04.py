ventes = [
    {"produit": "café", "prix": 2.5, "quantite":120},
    {"produit": "thé", "prix": 2.0, "quantite":80},
    {"produit": "chocolat", "prix": 3.5, "quantite":45},
]

#1

ca_par_produit = {}

for produit in ventes:
    ca = produit["prix"] * produit["quantite"]
    ca_par_produit[produit["produit"]] = ca

print(ca_par_produit)

#2

print(f"Total CA: {sum(ca_par_produit.values())}")

#3

print(f"Meilleur produit: {max(ca_par_produit, key=ca_par_produit.get)}")
