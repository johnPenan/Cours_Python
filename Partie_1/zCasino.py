import os
# Importation des modules random et math
from random import randrange
from math import ceil

# Ce programme est un jeu de Casino dont les numéros varient de 0 à 49

#Declaration du montant d'argent initial, gain initial et la volonté de jouer au Casino 
argent = 100
gain = 0
jeu = True
# Demander le nom du joeur
nom = input("Donnez votre nom:")
print("Bienvenue {} dans le jeu zCasino...!".format(nom)) 

while jeu and argent > 0:
    print("Votre argent actuel du jeu est:{}$".format(argent))
    # Demander au croupier de lancer la roulette
    numero_bille = randrange(50)
    print("Bille:", numero_bille)
    # Demander au joueur de choisir un numéro
    mise = int(input("Veillez donner le nombre sur lequel vous souhaitez mise (entre 0 et 49):"))
    # Demander au joueur de faire sa mise
    montant_mise = int(input("Veillez saisir le montant de la mise:"))
    
    if mise == numero_bille:
        argent += 3*montant_mise
        print("Le joueur {} a gagné {}$.".format(nom,montant_mise))
        
    elif mise % 2 == numero_bille % 2:    
        gain = ceil(montant_mise / 2)
        argent += gain
        print("Pair: Le joueur {} a gagné {}$ qui vaut 50% de la mise de {}$.".format(nom,gain,montant_mise))
    else:
        argent -= montant_mise
        print("Le joueur {} a perdu sa mise de {}$".format(nom, montant_mise))

print("Courage {}, vous avez perdu la partie...!".format(nom))
    
    
os.system("pause")