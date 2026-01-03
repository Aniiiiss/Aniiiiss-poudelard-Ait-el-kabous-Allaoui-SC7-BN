from utils.input_utils import demander_nombre
from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre_4
from chapitres.chapitre_5 import lancer_chapitre_5


def afficher_menu():
    print("=== Menu principal de Poudlard ===")
    print("1. Lancer l'aventure")
    print("2. Quitter le jeu")


def lancer_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0,
    }

    en_cours = True
    while en_cours:
        afficher_menu()
        choix = demander_nombre("Votre choix : ", 1, 2)

        if choix == 1:
            # Chapitre 1 : création du personnage
            personnage = lancer_chapitre_1()

            # Chapitre 2 : voyage + répartition ( garde le retour + passe maisons si votre fonction le demande)
            personnage = lancer_chapitre_2(personnage, maisons)

            # Chapitre 3 : apprentissage des sorts + quiz (met à jour maisons)
            lancer_chapitre_3(personnage, maisons)

            # Chapitre 4 : Quidditch / fin d'année
            lancer_chapitre_4(personnage, maisons)

            #  Chapitre 5 : boutique (extension)
            personnage = lancer_chapitre_5(personnage, maisons)

        elif choix == 2:
            print("Merci d'avoir joué à Poudlard, à bientôt jeune sorcier !")
            en_cours = False
