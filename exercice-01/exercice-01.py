
#1.
produit = "Clavier"
prix_ht = 19.90
quantite = 3
taux_tva = 0.20
#2.
total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)
#3.
print(f"Le total HT pour {quantite} {produit}(s) est de {total_ht:.2f} €")
print(f"Le total TTC pour {quantite} {produit}(s) est de {total_ttc:.2f} €")
#4
int(prix_ht)

total_ht = prix_ht * quantite
total_ttc = total_ht * (1 + taux_tva)
