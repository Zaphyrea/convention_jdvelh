from hero import Visiteur
from narrator import Narrator
from connection import Connexion
from data import Data
import random

def create_character():
    character_name = input("Votre ticket s'il vous plaît. Comment souhaitez-vous être appelé ? ")
    print("Quel est votre team ? 1) Cosplayeur, 2) Fan d'anime, 3) Furry")
    role_choice = input("Faites votre choix avec précaution (1/2/3): ")

    roles = {"1": "Cosplayeur", "2": "Fan d'animés", "3": "Furry"}
    specialisation = roles.get(role_choice, "Cosplayeur")  # Choix par défaut
    return character_name, specialisation


def get_character_info(personnage_joueur):
    character_name = personnage_joueur.get_nom()
    character_type = type(personnage_joueur).__name__
    character_charisme = personnage_joueur.get_charisme()

    # Create a formatted string with character info
    character_info = (
        f"Vous êtes un {character_type} hors du commun, répondant au doux nom de {character_name}, "
        f"vaillant {character_type} prêt à affronter la foule. Malgré le départ de votre camarade, vous décidez de continuer l'aventure. Vos caractéristiques sont les suivantes:\n"
        f"Charisme: {character_charisme}"
    )
    return character_info

def generer_salles(nombre_salles, charisme_joueur):
    # Liste des types de salle possibles
    types_salle = [
        "Stand avec un vendeur qui vous donne un goodie qui donne des points de charisme aléatoires.",
        "Rencontre avec un personnage qui vous propose un freehug et une photo.",
        "Conférence pour négocier un access backstage qui vous permet de gagner le jeu.",
        "Salle de concours de cosplay, où vous pouvez gagner des points de charisme en participant.",
        "Salle de projection d'un nouvel animé, les fans reçoivent des points de charisme bonus.",
        "Salle de jeux vidéo, où vous pouvez jouer à des jeux pour gagner des points de charisme.",
        "Salle de karaoké, où vous pouvez chanter pour obtenir des points de charisme.",
        "Salle de vente aux enchères d'articles rares, avec une chance de gagner des points de charisme.",
        "Salle de rencontres avec des invités spéciaux, qui peuvent vous donner des points de charisme.",
        "Salle de réalité virtuelle, où vous pouvez vivre des aventures pour gagner des points de charisme.",
        "Salle VIP avec Gwendal, le célèbre artiste manga."
    ]

    # Générer des salles aléatoires
    nombre_salles = min(nombre_salles, len(types_salle))  # Limit the number of requested rooms
    salles = random.sample(types_salle, nombre_salles)

    # Insérer une salle de détente avec Gwendal aléatoirement
    salle_gwendal = "Salle VIP avec Gwendal, le célèbre artiste manga."
    index_insertion = random.randint(0, nombre_salles - 1)
    salles.insert(index_insertion, salle_gwendal)

    return salles

def get_difficulte():
    print("Choisissez la difficulté:")
    print("1. Tokyo market Brest (facile)")
    print("2. Japan Vannes (Moyen)")
    print("3. Paris manga (difficile)")
    choix = input("Choisissez le niveau de difficulté (1/2/3): ")

    difficulte = "Tokyo market Brest"
    nombre_salles = 20

    if choix == "2":
        difficulte = "Japan Vannes"
        nombre_salles = 15
    elif choix == "3":
        difficulte = "Paris manga "
        nombre_salles = 8

    return difficulte, nombre_salles

# Fonction de description du contexte de départ
def narration_lieu():
    narrator = Narrator()
    narration = narrator.get_description_lieu()  # Call the method to get narration
    print(narration)

# Fonction principale du jeu
def main():
    # Obtenir le niveau de difficulté choisi par le joueur
    difficulte, nombre_salles = get_difficulte()

    # Créer le personnage du joueur
    character_name, specialisation = create_character()
    player = Visiteur(character_name, specialisation)

    # Afficher les informations sur le personnage
    print(get_character_info(player))

    # Générer et afficher les salles du donjon
    salles = generer_salles(nombre_salles, player.get_charisme())

    print(f"\nBienvenue à la convention ({difficulte}) ! Vous entrez dans la première salle :")
    print(f"{salles[0]}\n")

    # Description rapide du contexte par l'API
    narration_lieu()

    # Boucle de jeu
    current_room = 0
    total_charisme_gagne = 0  # Variable pour suivre le total des points de charisme gagnés
    while player.get_charisme() > 0 and current_room < len(salles):
        # Déplacer la mise à jour de la variable salle_type à l'intérieur de la boucle
        salle_type = salles[current_room].split("-")[0].strip()

        print("Que voulez-vous faire ?")
        print("1. Se balader dans la convention")

        # Actions spécifiques en fonction du type de salle actuelle
        salle_type = salles[current_room].split("-")[0].strip()
        if salle_type == "Stand avec un vendeur qui vous donne un goodie qui donne des points de charisme aléatoires.":
            print("2. Obtenir un goodie du vendeur")
        elif salle_type == "Rencontre avec un personnage qui vous propose un freehug et une photo.":
            print("2. Faire un freehug et prendre une photo avec le personnage")
        elif salle_type == "Conférence pour négocier un access backstage qui vous permet de gagner le jeu.":
            print("2. Assister à la conférence pour négocier l'accès backstage")
        elif salle_type == "Salle de concours de cosplay, où vous pouvez gagner des points de charisme en participant.":
            print("2. Participer au concours de cosplay")
        elif salle_type == "Salle de projection d'un nouvel animé, les fans reçoivent des points de charisme bonus.":
            print("2. Regarder la projection de l'animé")
        elif salle_type == "Salle de jeux vidéo, où vous pouvez jouer à des jeux pour gagner des points de charisme.":
            print("2. Jouer à des jeux vidéo")
        elif salle_type == "Salle de karaoké, où vous pouvez chanter pour obtenir des points de charisme.":
            print("2. Chanter au karaoké")
        elif salle_type == "Salle de vente aux enchères d'articles rares, avec une chance de gagner des points de charisme.":
            print("2. Participer à la vente aux enchères")
        elif salle_type == "Salle de rencontres avec des invités spéciaux, qui peuvent vous donner des points de charisme.":
            print("2. Rencontrer les invités spéciaux")
        elif salle_type == "Salle de réalité virtuelle, où vous pouvez vivre des aventures pour gagner des points de charisme.":
            print("2. Plonger dans l'aventure en réalité virtuelle")
        elif salle_type == "Salle VIP avec Gwendal, le célèbre développeur de jeux vidéos dont vous êtes le héros.":
            print("2. Rdv en salle VIP pour rencontrer avec Gwendal")

        print("3. Afficher le nombre de points de charisme")
        print("4. Quitter la convention")
        choix = input("Choisissez l'action à effectuer (1/2/3/4): ")

        if choix == "1":
            # Explorer la salle actuelle
            print(f"Vous explorez la salle {current_room + 1}: {salles[current_room]}\n")

            # Mettre à jour la salle actuelle pour passer à la suivante
            current_room += 1

        elif choix == "2":
            # Actions spécifiques en fonction du type de salle actuelle (ajoutez les actions pour chaque salle ici)
            if salle_type == "Stand avec un vendeur qui vous donne un goodie qui donne des points de charisme aléatoires.":
                print("Vous obtenez un goodie du vendeur.")
                # Générer un nombre aléatoire de points de charisme gagnés entre 5 et 15
                points_charisme_gagnes = random.randint(5, 15)
                # Générer aléatoirement si le joueur perd des points de charisme
                if random.random() < 0.2:  # 20% de chance de perdre des points
                    points_charisme_gagnes *= -1  # Perdre des points de charisme
                    print("Malheureusement, le goodie est moche et vous fait perdre des points de charisme.")
                else:
                    print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")
                player.charisme += points_charisme_gagnes
                total_charisme_gagne += points_charisme_gagnes
                print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")
            elif salle_type == "Salle VIP avec Gwendal, le célèbre développeur de jeux vidéos dont vous êtes le héros.":
                print("Vous entrez dans la salle VIP et rencontrez Gwendal, le célèbre développeur du jeu Convention_Adventure ! .")
                if player.get_charisme() >= 50:
                    print("Impressionné par votre charisme élevé, Gwendal décide de vous aider !")
                    print("Il vous donne tous les goodies disponibles et un Pass backstage pour gagner le jeu.")
                    print("Félicitations! Vous avez impressionné tout le monde avec votre charisme dévastateur! Votre aura pousse presque les gens à s'évanouir sur votre passage.")
                else:
                    print("Gwendal vous ignore, déçu par votre manque de charisme.")
                    print("Vous réalisez que vous n'êtes pas assez charismatique pour obtenir son aide.")
                    print("Votre aventure prend fin ici. Vous quittez la convention, vos rêves de gloire ont éclaté avant même que vous ne puissiez l'effleurer...")
                    break
            elif salle_type == "Rencontre avec un personnage qui vous propose un freehug et une photo.":
                print("Vous faites un freehug et prenez une photo avec le personnage.")
                points_charisme_gagnes = random.randint(5, 15)
                # Générer aléatoirement si le joueur perd des points de charisme
                if random.random() < 0.2:  # 20% de chance de perdre des points
                    points_charisme_gagnes *= -1  # Perdre des points de charisme
                    print("Comment osez-vous refuser un freehug et une photo ! Votre charisme diminue!")
                else:
                    print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")
                player.charisme += points_charisme_gagnes
                total_charisme_gagne += points_charisme_gagnes
                print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")
            elif salle_type == "Conférence pour négocier un accès backstage qui vous permet de gagner le jeu.":
                print("Vous assistez à la conférence et négociez un accès backstage.")
                points_charisme_gagnes = random.randint(5, 15)
                # Générer aléatoirement si le joueur perd des points de charisme
                if random.random() < 0.2:  # 20% de chance de perdre des points
                    points_charisme_gagnes *= -1  # Perdre des points de charisme
                    print("Malheureusement, aucun conférencier ne vous remarque. Votre égo prend une claque, votre charisme diminue.")
                else:
                    print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")
                player.charisme += points_charisme_gagnes
                total_charisme_gagne += points_charisme_gagnes
                print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")
            elif salle_type == "Salle de concours de cosplay, où vous pouvez gagner des points de charisme en participant.":
                print("Vous participez au concours de cosplay.")
                points_charisme_gagnes = random.randint(5, 15)
                # Générer aléatoirement si le joueur perd des points de charisme
                if random.random() < 0.2:  # 20% de chance de perdre des points
                    points_charisme_gagnes *= -1  # Perdre des points de charisme
                    print("Malheureusement, votre cosplay n'était pas au goût de tout le monde. Vous vous ridiculisez sur scène et perdez du charisme.")
                else:
                    print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")
                player.charisme += points_charisme_gagnes
                total_charisme_gagne += points_charisme_gagnes
                print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")
            elif salle_type == "Salle de projection d'un nouvel animé, les fans reçoivent des points de charisme bonus.":
                # Récupérer un animé aléatoire de la table 'animes'
                with Connexion.connecter() as bdd:
                    # Créer un curseur pour exécuter des requêtes SQL
                    with bdd.cursor() as cursor:
                        cursor.execute("SELECT Titre, Resume FROM animes ORDER BY RAND() LIMIT 1")
                        anime = cursor.fetchone()

                        # Vérifier si une ligne a été trouvée
                        if anime is not None:
                            # Afficher l'animé aléatoire
                            print(f"Vous regardez la projection de l'animé : {anime[0]}")
                            print(f"Résumé : {anime[1]}")

                            # Générer aléatoirement si le joueur perd des points de charisme
                            if random.random() < 0.2:  # 20% de chance de perdre des points
                                points_charisme_gagnes = random.randint(-15, -5)  # Perdre des points de charisme
                                print("Malheureusement, cet animé n'était pas à la hauteur de votre temps... Votre déception se lit sur votre visage, ce qui fait chuter votre charisme.")
                            else:
                                points_charisme_gagnes = random.randint(5, 15)  # Gagner des points de charisme
                                print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")

                            # Mettre à jour le charisme du joueur
                            player.charisme += points_charisme_gagnes
                            total_charisme_gagne += points_charisme_gagnes
                            print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")
                        else:
                            print("Désolé, le projecteur a un dysfonctionnement, la projection est annulée.\n")

            elif salle_type == "Salle de jeux vidéo, où vous pouvez jouer à des jeux pour gagner des points de charisme.":
                print("Vous jouez à des jeux vidéo.")
                points_charisme_gagnes = random.randint(5, 15)
                # Générer aléatoirement si le joueur perd des points de charisme
                if random.random() < 0.2:  # 20% de chance de perdre des points
                    points_charisme_gagnes *= -1  # Perdre des points de charisme
                    print("Malheureusement, vous êtes un noob, vous perdez du charisme et un enfant se moque de vous.")
                else:
                    print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")
                player.charisme += points_charisme_gagnes
                total_charisme_gagne += points_charisme_gagnes
                print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")


            elif salle_type == "Salle de karaoké, où vous pouvez chanter pour obtenir des points de charisme.":
                print("Vous chantez au karaoké.")
                points_charisme_gagnes = random.randint(5, 15)
                # Générer aléatoirement si le joueur perd des points de charisme
                if random.random() < 0.2:  # 20% de chance de perdre des points
                    points_charisme_gagnes *= -1  # Perdre des points de charisme
                    print("Malheureusement, vous chantez comme une casserole. Le public vous lance des tomates. Vous n'avez plus aucune allure, votre charisme descend.")
                else:
                    print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")
                player.charisme += points_charisme_gagnes
                total_charisme_gagne += points_charisme_gagnes
                print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")


            elif salle_type == "Salle de vente aux enchères d'articles rares, avec une chance de gagner des points de charisme.":
                print("Vous participez à la vente aux enchères.")
                points_charisme_gagnes = random.randint(5, 15)
                # Générer aléatoirement si le joueur perd des points de charisme
                if random.random() < 0.2:  # 20% de chance de perdre des points
                    points_charisme_gagnes *= -1  # Perdre des points de charisme
                    print("Malheureusement, vous ne possédez pas assez de thunes, vous n'êtes pas à l'aise financièrement. On n'enchérit pas si on ne peut pas, votre charisme diminue.")
                else:
                    print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")
                player.charisme += points_charisme_gagnes
                total_charisme_gagne += points_charisme_gagnes
                print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")

            elif salle_type == "Salle de rencontres avec des invités spéciaux, qui peuvent vous donner des points de charisme.":
                print("Vous rencontrez les invités spéciaux.")

                # Récupérer la connexion à la base de données
                bdd = Connexion.connecter()

                # Créer un curseur pour exécuter des requêtes SQL
                cursor = bdd.cursor()

                # Récupérer un invité spécial aléatoire de la table 'celebrites'
                cursor.execute("SELECT Nom FROM celebrites ORDER BY RAND() LIMIT 1")
                celebrity = cursor.fetchone()

                # Vérifier si une ligne a été trouvée
                if celebrity is not None:
                    # Ici, celebrity est un tuple avec un seul élément correspondant au nom de l'invité spécial
                    # Pour accéder au nom, utilisez l'index 0
                    celebrity_name = celebrity[0]

                    # Afficher l'invité spécial aléatoire
                    print(f"Vous rencontrez {celebrity_name} !")

                    # Générer aléatoirement si le joueur perd des points de charisme
                    if random.random() < 0.2:  # 20% de chance de perdre des points
                        points_charisme_gagnes = random.randint(-15, -5)  # Perdre des points de charisme
                        print(f"Malheureusement, {celebrity_name} ne vous écoute pas. Votre égo se ramasse une gigantesque claque. Votre charisme dégringole.")
                    else:
                        points_charisme_gagnes = random.randint(5, 15)  # Gagner des points de charisme
                        print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")

                    # Mettre à jour le charisme du joueur
                    player.charisme += points_charisme_gagnes
                    total_charisme_gagne += points_charisme_gagnes
                    print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")
                else:
                    print("Désolé, l'invité spécial est resté bloqué dans les bouchons. Une autre fois peut-être.\n")

                # Fermer le curseur et la connexion à la base de données
                cursor.close()
                bdd.close()

        elif salle_type == "Salle de réalité virtuelle, où vous pouvez vivre des aventures pour gagner des points de charisme.":
            print("Vous plongez dans l'aventure en réalité virtuelle.")
            points_charisme_gagnes = random.randint(5, 15)
            # Générer aléatoirement si le joueur perd des points de charisme
            if random.random() < 0.2:  # 20% de chance de perdre des points
                points_charisme_gagnes *= -1  # Perdre des points de charisme
                print("Malheureusement, vous vous étalez en vous prenant le pied dans une chaise. Avec le nez en sang vous perdez en charisme.")
            else:
                print(f"Vous avez gagné {points_charisme_gagnes} points de charisme !")
            player.charisme += points_charisme_gagnes
            total_charisme_gagne += points_charisme_gagnes
            print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")

        elif choix == "3":
            # Afficher le nombre de points de charisme
            print(f"Vous avez actuellement {player.get_charisme()} points de charisme.\n")

        elif choix == "4":
            # Quitter la convention
            print("Vous quittez la convention.")
            print("Merci d'avoir joué à Convention_Adventure !")
            break

        else:
            print("Choix invalide. Veuillez choisir une action valide.\n")

    # Vérifier si le joueur a gagné ou perdu le jeu
    if player.get_charisme() <= 0:
        print("Vous avez perdu toutes vos énergies charismatiques!")
        print("Votre aventure prend fin ici. Vous quittez la convention, vos rêves de gloire ont éclaté avant même que vous ne puissiez l'effleurer...")
    elif current_room >= len(salles):
        print("Félicitations! Vous avez impressionné tout le monde avec votre charisme dévastateur! Votre aura pousse presque les gens à s'évanouir sur votre passage!")
        print(f"Vous avez accumulé un total de {total_charisme_gagne} points de charisme.")
        print("Vous êtes désormais tellement célèbre que vous serez invité en VIP à la prochaine convention!")

if __name__ == "__main__":
    main()
