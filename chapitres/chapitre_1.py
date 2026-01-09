from utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier
from univers.personnage import initialiser_personnage, afficher_personnage, modifier_argent, ajouter_objet

def _normaliser_catalogue(inventaire_json):
    """
    Transforme le contenu de inventaire.json en une liste de tuples (nom, prix).
    Supporte plusieurs formats possibles.
    """
    catalogue = []

    # Format 1 : liste de dict
    if isinstance(inventaire_json, list):
        for item in inventaire_json:
            if isinstance(item, dict):
                nom = item.get("nom") or item.get("name") or item.get("objet")
                prix = item.get("prix") or item.get("price")
                if nom is not None and prix is not None:
                    catalogue.append((str(nom), int(prix)))

    # Format 2 : dict {"Objet": 10} OU {"Objet": {"prix": 10}}
    elif isinstance(inventaire_json, dict):
        for k, v in inventaire_json.items():
            if isinstance(v, dict) and "prix" in v:
                catalogue.append((str(k), int(v["prix"])))
            elif isinstance(v, (int, float)):
                catalogue.append((str(k), int(v)))

        # Format 3 : dict de sous-dicts (au cas où)
        if len(catalogue) == 0:
            for sous in inventaire_json.values():
                if isinstance(sous, dict):
                    for k, v in sous.items():
                        if isinstance(v, dict) and "prix" in v:
                            catalogue.append((str(k), int(v["prix"])))
                        elif isinstance(v, (int, float)):
                            catalogue.append((str(k), int(v)))

    return catalogue

def introduction():
    print("====== Chapitre 1 : L'arrivée dans le monde magique ======")
    print("Depuis toujours, votre vie ressemble à celle de n'importe qui d'autres.")
    print("Les mêmes rues, les mêmes habitudes... rien qui laisse penser que vous êtes différent(e).")
    print("Et pourtant, quelque chose a toujours semblé... étrange. Comme si vous étiez destiné(e) à autre chose.")
    print("\nTout bascule ce matin-là.")
    print("Un bruit sec résonne à votre fenêtre. Une simple enveloppe... mais scellée d'un blason inconnu.")
    print("Votre aventure commence ici. À vous de découvrir qui vous êtes vraiment.\n")

    input("Appuyez sur Entrée pour ouvrir la lettre...")


def creer_personnage():
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")

    print("\nAttribuez vos caractéristiques (valeurs entre 1 et 10).")
    courage = demander_nombre("courage : ", 1, 10)
    intelligence = demander_nombre("intelligence : ", 1, 10)
    loyaute = demander_nombre("loyauté : ", 1, 10)
    ambition = demander_nombre("ambition : ", 1, 10)

    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,   # correction de la faute 'layauté'
        "ambition": ambition,
    }

    personnage = initialiser_personnage(nom, prenom, attributs)

    print("\nVoici votre personnage :")
    afficher_personnage(personnage)

    return personnage


def recevoir_lettre():
    print("\nUne chouette se pose devant toi et laisse tomber une enveloppe.")
    print("Le parchemin est épais, l'écriture élégante, et un blason inconnu est scellé en rouge.\n")

    print("« Nous avons le plaisir de vous informer que vous avez été admis(e) à l'École de Magie de Poudlard. »")
    print("« Les cours débuteront le 1er septembre. »\n")

    choix = demander_choix(
        "Que décidez-vous de faire ?",
        ["Accepter l'invitation", "Refuser et rester chez vous"]
    )

    if choix == "Refuser et rester chez vous":
        print("\nVous jetez la lettre à la poubelle.")
        print("La magie n'était visiblement pas faite pour vous.")
        print("Vous finissez votre vie à regarder la télé. Fin de l'aventure ")
        exit(0)

    print("\n. Une nouvelle vie vous attend.")
    print("Vous acceptez l'invitation et préparez vos valises...\n")


def rencontrer_hagrid(personnage):
    print("\nUne silhouette gigantesque apparaît devant vous.")
    print("Sa barbe est épaisse, son manteau immense, et son sourire rassurant.\n")

    print("Hagrid : \"Salut ! Je m'appelle Hagrid. Je suis venu t’aider à faire tes achats")
    print("pour Poudlard, sur le Chemin de Traverse.\" \n")

    choix = demander_choix(
        "Voulez-vous suivre Hagrid ?",
        ["Oui", "Non"]
    )

    if choix == "Non":
        print("\nHagrid insiste gentiment et vous entraîne quand même avec lui !")
    else:
        print("\nVous suivez Hagrid sans hésiter.")

    input("Appuyez sur Entrée pour continuer vers le Chemin de Traverse...")

def acheter_fournitures(personnage):
    print("\nBienvenue sur le Chemin de Traverse !")

    inventaire_json = load_fichier("data/inventaire.json")
    catalogue = _normaliser_catalogue(inventaire_json)

    if len(catalogue) == 0:
        print("Erreur : catalogue vide ou format inventaire.json non reconnu.")
        exit(1)

    print("Catalogue des objets disponibles :")
    for i, (nom, prix) in enumerate(catalogue, start=1):
        print(f"{i}. {nom} - {prix} galions")

    obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    achetes = set()

    # Boucle d’achats jusqu’à ce que tout soit acheté
    while len(obligatoires) > 0:
        argent = personnage.get("Argent", 0)
        print(f"\nVous avez {argent} galions.")
        print("Objets obligatoires restant à acheter :", ", ".join(obligatoires))

        choix_num = demander_nombre("Entrez le numéro de l'objet à acheter : ", 1, len(catalogue))
        nom_objet, prix_objet = catalogue[choix_num - 1]

        if argent < prix_objet:
            print("Vous n'avez pas assez d'argent pour cet achat. Vous perdez la partie !")
            exit(0)

        if nom_objet in achetes:
            print("Vous avez déjà acheté cet objet.")
            continue

        modifier_argent(personnage, -prix_objet)
        ajouter_objet(personnage, "Inventaire", nom_objet)
        achetes.add(nom_objet)
        print(f"Vous avez acheté : {nom_objet} (-{prix_objet} galions).")

        if nom_objet in obligatoires:
            obligatoires.remove(nom_objet)

    print("\nTous les objets obligatoires ont été achetés !")

    # Choix de l'animal de compagnie
    animaux = [("Chouette", 20), ("Chat", 15), ("Rat", 10), ("Crapaud", 5)]

    argent = personnage.get("Argent", 0)
    print(f"\nIl est temps de choisir votre animal de compagnie pour Poudlard ! Vous avez {argent} galions.")
    print("Voici les animaux disponibles :")
    for i, (nom, prix) in enumerate(animaux, start=1):
        print(f"{i}. {nom} - {prix} galions")

    choix_animal = demander_nombre("Votre choix : ", 1, len(animaux))
    nom_animal, prix_animal = animaux[choix_animal - 1]

    argent = personnage.get("Argent", 0)
    if argent < prix_animal:
        print("Vous n'avez pas assez d'argent pour cet animal. Vous perdez la partie !")
        exit(0)

    modifier_argent(personnage, -prix_animal)
    ajouter_objet(personnage, "Inventaire", nom_animal)
    print(f"Vous avez choisi : {nom_animal} (-{prix_animal} galions).")

    print("\nTous les objets obligatoires ont été achetés avec succès ! Voici votre inventaire final :")
    afficher_personnage(personnage)


def lancer_chapitre_1():
    introduction()
    personnage = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(personnage)
    acheter_fournitures(personnage)

    print("\n=== Fin du Chapitre 1 ===")
    print("Votre aventure commence à Poudlard...\n")

    return personnage

