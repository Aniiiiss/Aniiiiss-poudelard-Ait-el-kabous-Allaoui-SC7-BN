import random
from utils.input_utils import demander_nombre, demander_choix, load_fichier
from univers.personnage import afficher_personnage, modifier_argent, ajouter_objet
from univers.maison import actualiser_points_maison


def _titre(txt):
    print("\n" + "═" * 60)
    print(txt)
    print("═" * 60 + "\n")


def _maison(personnage):
    return personnage.get("Maison") or personnage.get("maison")


def _argent(personnage):
    # On essaie d’être compatible avec différentes clés
    if "Argent" in personnage:
        return personnage.get("Argent", 0)
    return personnage.get("argent", 0)


def _catalogue_depuis_json(data):
    catalogue = []

    # Format liste : [{"nom": "...", "prix": 10}, ...]
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                nom = item.get("nom") or item.get("name") or item.get("objet")
                prix = item.get("prix") or item.get("price")
                if nom is not None and prix is not None:
                    catalogue.append((nom, int(prix)))

    # Format dict : {"Objet": 10} ou {"Objet": {"prix": 10}}
    elif isinstance(data, dict):
        for nom, val in data.items():
            if isinstance(val, dict) and "prix" in val:
                catalogue.append((nom, int(val["prix"])))
            elif isinstance(val, (int, float)):
                catalogue.append((nom, int(val)))

        # Rare : sous-dictionnaires
        if len(catalogue) == 0:
            for sous in data.values():
                if isinstance(sous, dict):
                    for nom, val in sous.items():
                        if isinstance(val, dict) and "prix" in val:
                            catalogue.append((nom, int(val["prix"])))
                        elif isinstance(val, (int, float)):
                            catalogue.append((nom, int(val)))

    return catalogue


def _type_demande(prix):
    if prix <= 10:
        return "pas cher"
    if prix >= 40:
        return "rare"
    return "standard"


def _afficher_stock(stock):
    print(" Ton petit stock du jour :")
    vide = True
    for nom, qte in stock.items():
        if qte > 0:
            print(f"  • {nom} x{qte}")
            vide = False
    if vide:
        print("  (vide… et ça sent la fermeture )")
    print()


def _tirer_client(catalogue, stock):
    prénoms = ["Nolan", "Lina", "Farah", "Yanis", "Maya", "Hugo", "Inès", "Sami", "Jade", "Adam"]
    humeur = ["pressé", "curieux", "méfiant", "enthousiaste", "fatigué", "très exigeant"]

    demande = random.choice(["pas cher", "standard", "rare"])
    client = random.choice(prénoms)
    etat = random.choice(humeur)

    possibles = []
    for nom, prix in catalogue:
        if stock.get(nom, 0) > 0 and _type_demande(prix) == demande:
            possibles.append((nom, prix))

    # si rien du bon type : on prend n’importe quoi en stock
    if len(possibles) == 0:
        for nom, prix in catalogue:
            if stock.get(nom, 0) > 0:
                possibles.append((nom, prix))

    if len(possibles) == 0:
        return None

    return client, etat, demande, random.choice(possibles)


def _acheter_stock_depart(personnage, catalogue):
    _titre("Chapitre 5 — Une journée de boutique au Chemin de Traverse")

    print("Hagrid te pousse gentiment devant une petite boutique…")
    print("Hagrid : « Je te la confie pour la journée. Fais pas exploser la caisse, hein. » \n")

    print(f" Tu regardes ta bourse : {_argent(personnage)} gallions.")
    print("Tu dois acheter un petit stock de départ avant d’ouvrir.\n")

    print(" Catalogue (prix d’achat) :")
    for i, (nom, prix) in enumerate(catalogue, start=1):
        print(f"  {i}. {nom} — {prix} gallions")

    stock = {}
    achats = 5

    print("\nTu peux faire jusqu’à 5 achats (avec quantité 1 à 3).")
    print("Astuce : n’achète pas que du cher… les clients aiment aussi le 'pas cher'.\n")

    while achats > 0:
        argent = _argent(personnage)
        if argent <= 0:
            print("Oups… tu n’as plus un gallion. Fin des achats.")
            break

        choix = demander_choix("🛒 Action :", ["Acheter quelque chose", "Ouvrir la boutique maintenant"])
        if choix == "Ouvrir la boutique maintenant":
            break

        num = demander_nombre("Numéro de l’objet : ", 1, len(catalogue))
        nom_obj, prix_obj = catalogue[num - 1]

        qte = demander_nombre("Quantité (1 à 3) : ", 1, 3)
        cout = prix_obj * qte

        if argent < cout:
            print(" Tu fouilles tes poches… pas assez. Essaie une quantité plus petite.\n")
            continue

        modifier_argent(personnage, -cout)
        stock[nom_obj] = stock.get(nom_obj, 0) + qte
        achats -= 1

        print(f" Ajout au stock : {nom_obj} x{qte} (-{cout} gallions)")
        print(f" Il te reste : {_argent(personnage)} gallions.\n")

    if sum(stock.values()) == 0:
        print("Tu n’as rien acheté…")
        print("Hagrid : « Bon… on va éviter d’appeler ça une boutique alors. » ")
        return None

    input("Appuie sur Entrée… *la clochette de la porte tinte* ")
    return stock


def lancer_chapitre_5(personnage, maisons):
    data = load_fichier("data/inventaire.json")
    catalogue = _catalogue_depuis_json(data)

    if len(catalogue) == 0:
        print("Erreur : impossible de lire inventaire.json (format vide ou inattendu).")
        return personnage

    stock = _acheter_stock_depart(personnage, catalogue)
    if stock is None:
        return personnage

    _titre("La boutique est ouverte !")

    reputation = 50   # 0 à 100
    profit = 0

    prix_achat = {}
    for nom, prix in catalogue:
        prix_achat[nom] = prix

    nb_clients = 8
    for i in range(1, nb_clients + 1):
        print(f"🧍 Client {i}/{nb_clients}")
        _afficher_stock(stock)
        print(f" Réputation : {reputation}/100")
        print(f" Gallions (perso) : {_argent(personnage)}\n")

        tirage = _tirer_client(catalogue, stock)
        if tirage is None:
            print("Plus rien à vendre… tu fermes plus tôt.")
            break

        client, etat, demande, (objet, prix_obj) = tirage

        facteur = random.randint(90, 120)
        bonus_rep = (reputation - 50) // 5
        volonte = prix_obj + (prix_obj * facteur) // 100 + bonus_rep

        print(f"{client} ({etat}) : « Bonjour… je cherche un truc {demande}. »")
        print(f"Il/elle regarde : {objet} (ça t’a coûté {prix_obj} gallions)\n")

        action = demander_choix("Tu fais quoi ?", ["Je propose un prix", "Je refuse (et je le/la regarde partir)"])
        if action == "Je refuse (et je le/la regarde partir)":
            reputation -= 2
            if reputation < 0:
                reputation = 0
            print("Le client s’en va… pas très content. (-2 réputation)\n")
            continue

        prix_vente = demander_nombre("💬 Ton prix (1 à 200) : ", 1, 200)

        rem = demander_choix("Tu fais un geste commercial ?", ["Non", "Oui (-5 gallions)"])
        if rem == "Oui (-5 gallions)":
            prix_vente -= 5
            if prix_vente < 1:
                prix_vente = 1

        if prix_vente <= volonte:
            stock[objet] -= 1
            modifier_argent(personnage, prix_vente)

            benef = prix_vente - prix_achat[objet]
            profit += benef

            reputation += 2
            if reputation > 100:
                reputation = 100

            print(f" Vendu ! +{prix_vente} gallions. (bénéfice sur l’objet : {benef}) (+2 réputation)\n")
        else:
            reputation -= 4
            if reputation < 0:
                reputation = 0
            print(" « Trop cher… » Le client repose l’objet. (-4 réputation)\n")

        if reputation <= 10:
            print("Ta réputation est au fond du chaudron… tu fermes avant que ça tourne mal.")
            break

    _titre("Bilan de la journée")

    print(f" Bénéfice estimé : {profit} gallions")
    print(f" Réputation finale : {reputation}/100")
    print(f" Ton argent : {_argent(personnage)} gallions\n")

    maison = _maison(personnage)
    if maison is not None:
        points = 0

        if profit >= 30:
            points += 40
        elif profit >= 10:
            points += 20
        elif profit >= 0:
            points += 10
        else:
            points -= 10

        if reputation >= 80:
            points += 20
        elif reputation <= 20:
            points -= 10

        print(f" Ta maison ({maison}) reçoit {points} points.")
        actualiser_points_maison(maisons, maison, points)

    if profit >= 20 and reputation >= 60:
        print("\nUn client mystérieux glisse un petit objet sur le comptoir…")
        print("« Tu t’es bien débrouillé. Garde ça. »")
        print(" Tu obtiens : Amulette de chance\n")
        ajouter_objet(personnage, "Inventaire", "Amulette de chance")

    print(" Ton profil à la fin du chapitre 5 :\n")
    afficher_personnage(personnage)

    input("\nAppuie sur Entrée pour terminer le chapitre 5…")
    return personnage

