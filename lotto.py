# importation des bibliothèques

from datetime import *
from random import *
# definition de la fonction génératrice 
def generateur (annee, mois, jour , heure, minute, seconde):

    # création d'un objet datetime à partir des paramètre
    temps_defini = datetime(annee, mois,jour, heure, minute, seconde)

    # convertir l'objet en timestamp
    timestamp = temps_defini.timestamp()

    # initialiser le generateur
    seed(timestamp)
    # génerer 5 chiffres aléatoires entre 1 et 90
    nombre_aleatoire = [randint(1,90) for _ in range(5)]

    return nombre_aleatoire

# entrez les informations 
annee = int(input("Entrez l'année : "))
mois = int(input("Entrez le mois entre 1 et 12  : "))
if (1<= mois  <= 12):
    print("Vous pouvez continuer !!!!! ")
else:
    print("la valeur saisie est incorrecte ")
    exit() 
jour = int(input("Entrez le jour en 1 et 31 : "))
if (1<= jour <= 31):
    print("Vous pouvez continuer !!!!! ")
else:
    print("la valeur saisie est incorrecte ")
    exit()
heure = int(input("Entrez l'heure : "))
if (0<= heure <= 23):
    print("Vous pouvez continuer !!!!! ")
else:
    print("la valeur saisie est incorrecte ")
    exit()
minute = int(input("Entrez les minutes : "))
if (0<= minute <= 59):
    print("Vous pouvez continuer !!!!! ")
else:
    print("la valeur saisie est incorrecte ")
    exit()
seconde = int(input("Entrez les secondes : "))
if (0<= seconde <= 50):
    print("Vous pouvez continuer !!!!! ")
else:
    print("la valeur saisie est incorrecte ")
    exit()

nombres = generateur(annee,mois,jour,heure,minute,seconde)
print(nombres)

# FIN du programme de conçus par Jonathan Amani !!!!!!!!!





