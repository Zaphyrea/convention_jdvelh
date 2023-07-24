from connection import Connexion
import random

class Data:
    def __init__(self):
        self.cursor = Connexion.connecter()
    
    def get_random_goodie(self):
        self.cursor.execute("SELECT * FROM goodies")
        goodies = [goodie for goodie in self.cursor.fetchall()]
        return random.choice(goodies)


    def get_vendeur_aleatoire(self):
        # Requête SQL pour sélectionner toutes les données de la table 'vendeurs'
        self.cursor.execute("SELECT * FROM vendeurs")
        # Récupère toures les lignes de la table 'vendeurs' et les stocke dans une liste
        liste_vendeurs = [row for row in self.cursor.fetchall()]
        # Vérifier s'il y a des vendeurs dans la liste
        if not liste_vendeurs:
            return None
        # Sélection aléatoire d'un vendeur dans la liste
        vendeur_aleatoire = random.choice(liste_vendeurs)
        # Renvoie la ligne entière représentant le vendeur choisi
        return vendeur_aleatoire