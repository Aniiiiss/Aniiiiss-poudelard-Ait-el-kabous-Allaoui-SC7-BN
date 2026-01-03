from utils.input_utils import demander_choix, load_fichier
from univers.personnage import afficher_personnage
from univers.maison import repartition_maison


def _afficher_titre(titre):

    print("\n" + "=" * 60)
    print(titre)
    print("=" * 60 + "\n")


def rencontrer_amis(joueur):

    _afficher_titre(" Voyage vers Poudlard : premières rencontres")

    attributs = joueur.get("Attributs", {})


    print("Un garçon roux entre dans ton compartiment, l’air sympathique et un peu timide.")
    print('Ron : "Salut ! Moi c’est Ron Weasley. Je peux m’asseoir avec toi ?"')

    choix_ron = demander_choix(
        "Que réponds-tu ?",
        [
            "Bien sûr, assieds-toi !",
            "Je préfère voyager seul, désolé."
        ]
    )

    if choix_ron == "Bien sûr, assieds-toi !":
        attributs["loyaute"] = attributs.get("loyaute", 0) + 1
        print(" Tu acceptes Ron à tes côtés. Ta loyauté augmente de 1.")
    else:
        attributs["ambition"] = attributs.get("ambition", 0) + 1
        print(" Tu préfères voyager seul et réfléchir à ton avenir.")
        print("Ton ambition augmente de 1.")

    print("\nQuelques minutes plus tard, une jeune fille aux cheveux frisés ouvre la porte du compartiment.")
    print('Hermione : "Bonjour, je suis Hermione Granger. Tu as déjà lu tes manuels ?"')


    choix_hermione = demander_choix(
        "Comment réagis-tu ?",
        [
            "Oui, j’ai déjà commencé à tout lire !",
            "Euh... pas vraiment, je verrai plus tard."
        ]
    )

    if choix_hermione == "Oui, j’ai déjà commencé à tout lire !":
        attributs["intelligence"] = attributs.get("intelligence", 0) + 1
        print(" Hermione est impressionnée par ton sérieux.")
        print("Ton intelligence augmente de 1.")
    else:
        attributs["courage"] = attributs.get("courage", 0) + 1
        print(" Tu avoues honnêtement que tu n’as pas encore tout lu.")
        print("Ton courage augmente de 1.")


    print("\nPlus tard, un élève blond, à l’air hautain, passe devant ton compartiment.")
    print('Drago : "Alors, c’est toi le nouveau ? Tu ferais mieux de choisir les bons amis."')

    choix_drago = demander_choix(
        "Que fais-tu ?",
        [
            "L’ignorer et rester avec Ron et Hermione.",
            "Lui répondre sèchement.",
            "Essayer de rester poli."
        ]
    )

    if choix_drago == "L’ignorer et rester avec Ron et Hermione.":
        attributs["loyaute"] = attributs.get("loyaute", 0) + 1
        print(" Tu restes fidèle à tes nouveaux amis.")
        print("Ta loyauté augmente de 1.")
    elif choix_drago == "Lui répondre sèchement.":
        attributs["courage"] = attributs.get("courage", 0) + 1
        print("Tu ne te laisses pas intimider par Drago.")
        print("Ton courage augmente de 1.")
    else:
        attributs["intelligence"] = attributs.get("intelligence", 0) + 1
        print(" Tu restes calme et poli, sans te laisser manipuler.")
        print("Ton intelligence augmente de 1.")

    joueur["Attributs"] = attributs

    print("\nRésumé de tes attributs après le voyage :")
    print(joueur["Attributs"])

    input("\n(Appuie sur Entrée pour rejoindre le château et la Grande Salle...)")


def mot_de_bienvenue():

    _afficher_titre("Mot de bienvenue de Dumbledore")

    print("La Grande Salle est illuminée par des centaines de bougies flottantes.")
    print("Les quatre grandes tables des maisons sont pleines d’élèves qui chuchotent.")
    print("Au fond, la table des professeurs domine la salle avec Dumbledore au centre.\n")

    print("Dumbledore se lève, lève les bras, et le silence se fait...")
    print('Dumbledore : "Bienvenue à Poudlard, jeunes sorciers et jeunes sorcières !"')
    print('           "Ici, vous apprendrez la magie, mais aussi la valeur du courage,"')
    print('           "de la loyauté, de l’intelligence et de l’ambition."')
    print('           "Votre maison sera votre famille pendant ces années."')
    print('           "Que le festin commence, et que vos aventures soient inoubliables !"\n')

    input("(Appuie sur Entrée pour passer à la cérémonie de répartition...)")


def ceremonie_repartition(joueur):

    _afficher_titre(" Cérémonie de répartition")

    print("Les premières années se rassemblent devant le tabouret où repose le Choixpeau magique.\n")
    input("(Appuie sur Entrée pour t’avancer vers le Choixpeau...)")


    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            [
                "Je fonce l'aider",
                "Je réfléchis à un plan",
                "Je cherche de l’aide",
                "Je reste calme et j’observe"
            ],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            [
                "Courageux et loyal",
                "Rusé et ambitieux",
                "Patient et travailleur",
                "Intelligent et curieux"
            ],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            [
                "Fonces sans hésiter",
                "Cherches la meilleure stratégie",
                "Comptes sur tes amis",
                "Analyses le problème"
            ],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]

    print("\nLe Choixpeau se pose sur ta tête et murmure des questions...\n")

    maison = repartition_maison(joueur, questions)

    joueur["Maison"] = maison

    print(f"\nLe Choixpeau crie : {maison} !!!")
    print(f" Tu rejoins la maison {maison} sous les applaudissements !")

    input("\n(Appuie sur Entrée pour suivre les préfets vers ta salle commune...)")


def installation_salle_commune(joueur):

    _afficher_titre("🏰 Installation dans la salle commune")

    maison = joueur.get("Maison")

    if not maison:
        print("⚠ Erreur : aucune maison n’a été attribuée au joueur.")
        return

    print("Tu suis les préfets à travers les escaliers mouvants et les longs couloirs...\n")

    donnees_maisons = load_fichier("../data/maisons.json")

    infos_maison = donnees_maisons.get(maison, {})

    description = infos_maison.get("description_salle_commune", "")
    message_bienvenue = infos_maison.get("message_bienvenue", "")
    couleurs = infos_maison.get("couleurs", [])

    if description:
        print(description)
    else:
        print(f"Tu découvres la salle commune de {maison}, décorée aux couleurs de ta maison.")

    if message_bienvenue:
        print(message_bienvenue)
    else:
        print(f"Bienvenue dans la maison {maison} !")

    if isinstance(couleurs, list):
        texte_couleurs = ", ".join(str(c) for c in couleurs)
    else:
        texte_couleurs = str(couleurs)

    if texte_couleurs:
        print(f"Les couleurs de ta maison : {texte_couleurs}")

    input("\n(Appuie sur Entrée pour t’installer et passer au chapitre suivant...)")


def lancer_chapitre_2(personnage):

    _afficher_titre("📖 Chapitre 2 – Voyage vers Poudlard et sélection de la maison")

    rencontrer_amis(personnage)
    mot_de_bienvenue()
    ceremonie_repartition(personnage)
    installation_salle_commune(personnage)

    print("\n Fin du Chapitre 2 ! Voici l’état actuel de ton personnage :\n")
    afficher_personnage(personnage)

    print("\n Prépare-toi pour le Chapitre 3 : apprentissage de nouveaux sorts...\n")
