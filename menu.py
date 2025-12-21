
from utils.input_utils import demander_nombre


def afficher_menu_principal():

    print("\n=== MENU PRINCIPAL ===")
    print("1. Lancer le Chapitre 1 – L’arrivée dans le monde magique.")
    print("2. Quitter le jeu.")


def lancer_choix_menu():

    # 1. Initialise un dictionnaire maisons (points par maison)
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    while True:
        # 2. Affiche le menu
        afficher_menu_principal()

        # 3. Lit le choix (1 ou 2)
        choix = demander_nombre("Votre choix : ", 1, 2)

        # a) Si choix == 1 => lancer les chapitres successivement
        if choix == 1:
            # Chapitre 1
            from chapitres.chapitre_1 import lancer_chapitre_1
            personnage = lancer_chapitre_1()

            # Chapitre 2
            from chapitres.chapitre_2 import lancer_chapitre_2
            personnage = lancer_chapitre_2(personnage, maisons)

            # Chapitre 3
            from chapitres.chapitre_3 import lancer_chapitre_3
            lancer_chapitre_3(personnage, maisons)

            # Chapitre 4 (ou chapitre final selon votre sujet)
            from chapitres.chapitre_4 import lancer_chapitre_4
            lancer_chapitre_4(personnage, maisons)

        # b) Si choix == 2 => quitter
        elif choix == 2:
            print("\nMerci d'avoir joué ! À bientôt 👋")
            break

        # c) Sinon (normalement impossible grâce à demander_nombre)
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
