from utils.input_utils import demander_choix, load_fichier

from univers.maison import repartition_maison

from univers.personnage import afficher_personnage


def _afficher_titre(titre):

    print("\n" + "=" * 60)
    print(titre)
    print("=" * 60 + "\n")

def rencontrer_amis(joueur):
# 3.3.2.1 #
    _afficher_titre(" Voyage vers Poudlard : premières rencontres")

    # On récupère le dictionnaire des attributs du joueur
    attributs = joueur.get("Attributs", {})

    # Rencontre avec Ron
    print("Un garçon roux entre dans votre compartiment, l’air un peu timide mais très amical.")
    print("Ron : « Salut ! Moi c’est Ron Weasley. Je peux m’asseoir avec toi ? »")

    choix_ron = demander_choix(
        "Que répondez-vous ?",
        [
            "Bien sûr, assieds-toi !",
            "Je préfère voyager seul, désolé."
        ]
    )

    if choix_ron == "Bien sûr, assieds-toi !":
        # On valorise la loyauté
        attributs["loyauté"] = attributs.get("loyauté", 0) + 1
        print("🤝 Vous invitez Ron à s’asseoir. Votre loyauté augmente de 1.")
    else:
        # On valorise plutôt l’ambition (personnage plus solitaire)
        attributs["ambition"] = attributs.get("ambition", 0) + 1
        print("😼 Vous préférez rester seul pour réfléchir à votre avenir de grand sorcier.")
        print("Votre ambition augmente de 1.")

    print("Peu après, une jeune fille aux cheveux frisés ouvre la porte du compartiment.")

    # --- Rencontre avec Hermione ---
    print("Hermione : « Bonjour, je suis Hermione Granger. Vous avez déjà lu vos manuels ? »")

    choix_hermione = demander_choix(
        "Comment réagissez-vous ?",
        [
            "Oui, j’ai déjà commencé à tout lire !",
            "Euh… pas vraiment, je verrai plus tard."
        ]
    )

    if choix_hermione == "Oui, j’ai déjà commencé à tout lire !":
        attributs["intelligence"] = attributs.get("intelligence", 0) + 1
        print("📚 Hermione semble impressionnée par votre sérieux.")
        print("Votre intelligence augmente de 1.")
    else:
        attributs["courage"] = attributs.get("courage", 0) + 1
        print("😅 Vous avouez honnêtement que vous n’avez pas encore lu les manuels.")
        print("Il faut du courage pour l’admettre : votre courage augmente de 1.")

    # Rencontre avec Drago
    print("Plus tard, un élève blond à l’air hautain passe devant votre compartiment.")
    print("Drago : « Alors, c’est toi le nouveau ? Tu ferais mieux de choisir les bons amis. »")

    choix_drago = demander_choix(
        "Que faites-vous ?",
        [
            "L’ignorer et rester avec Ron et Hermione.",
            "Lui répondre sèchement.",
            "Essayer de rester poli."
        ]
    )

    if choix_drago == "L’ignorer et rester avec Ron et Hermione.":
        attributs["loyauté"] = attributs.get("loyauté", 0) + 1
        print("🤜🤛 Vous restez fidèle à vos nouveaux amis.")
        print("Votre loyauté augmente de 1.")
    elif choix_drago == "Lui répondre sèchement.":
        attributs["courage"] = attributs.get("courage", 0) + 1
        print(" Vous ne vous laissez pas intimider par Drago.")
        print("Votre courage augmente de 1.")
    else:
        attributs["intelligence"] = attributs.get("intelligence", 0) + 1
        print(" Vous restez calme et poli, sans vous laisser manipuler.")
        print("Votre intelligence augmente de 1.")


    joueur["Attributs"] = attributs

    print("Résumé de vos attributs après le voyage :")
    print(joueur["Attributs"])

    input("(Appuyez sur Entrée pour rejoindre le château et la Grande Salle...)")

