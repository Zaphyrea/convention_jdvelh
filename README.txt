# convention_jdvelh
Un jeu dont vous êtes le héros en cours de développement.
Certaines fonctionnalités ne sont pas encore effectives. La base de données est plus développée que nécessaire.

# Requirements
hugchat 
mysql-connector-python

# Précisions
Nous avons utilisé hugging chat pour donner "vie" au narrateur.
Il est nécessaire d'avoir un identifiant et un mot de passe pour (à rajouter dans le fichier 'narrator.py'  dans cette ligne : 'sign = Login("mail", "password")'

# Synopsis
Vous êtes un visiteur d'une convention orientée vers les animés, jeux vidéos et mangas. Un narrateur va vous donner rapidement un contexte et vous pourrez choisir ce que vous faites (déplacement, arrêter le jeu,...). Les conditions pour gagner ou perdre vont dépendre du nombre de points de charisme du personnage.


# Déroulement
--> Choix de la difficulté (3 niveaux). Plus on est proche de facile, plus il y aura de tours.
--> Création du personnage (nom, classe).
--> Durant chaque tour on va avoir le choix entre 4 possibilités :
	- se déplacer dans la salle suivante
	- réaliser l'action proposée
	- regarder les points de charisme
	- quitter la convention

