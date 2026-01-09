from utils.input_utils import demander_nombre
from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre4_quidditch
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
            personnage = lancer_chapitre_1()
            lancer_chapitre_2(personnage)
            lancer_chapitre_3(personnage, maisons)
            lancer_chapitre4_quidditch(personnage, maisons)
            personnage = lancer_chapitre_5(personnage, maisons)

        else:
            print("Merci d'avoir joué à Poudlard, à bientôt jeune sorcier !")
            en_cours = False

