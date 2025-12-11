
from utils.input_utils import demander_choix


def actualiser_points_maison(maisons, nom_maison, points):

    if nom_maison not in maisons:
        print(f"[Erreur] La maison '{nom_maison}' n'existe pas dans le dictionnaire.")
        return

    maisons[nom_maison] += points


def afficher_maison_gagnante(maisons):

    if not maisons:
        print("Aucune maison n'est définie.")
        return

    # Score maximum
    max_score = max(maisons.values())

    # Maisons qui ont ce score
    gagnantes = [nom for nom, score in maisons.items() if score == max_score]

    if len(gagnantes) == 1:
        nom = gagnantes[0]
        print(f"Maison gagnante : {nom} avec {max_score} points.")
    else:
        noms = ", ".join(gagnantes)
        print(f"Égalité entre les maisons : {noms} avec {max_score} points.")


def repartition_maison(joueur, questions):

    attributs = joueur.get("Attributs", {})

    # On récupère les attributs (en gérant éventuellement 'loyauté')
    courage = attributs.get("courage", 0)
    intelligence = attributs.get("intelligence", 0)
    loyaute = attributs.get("loyaute", attributs.get("loyauté", 0))
    ambition = attributs.get("ambition", 0)


    scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }

    # 1) Bonus de départ basé sur les attributs (pondération ×2 comme dans l’énoncé)
    scores["Gryffondor"] += courage * 2
    scores["Serpentard"] += ambition * 2
    scores["Poufsouffle"] += loyaute * 2
    scores["Serdaigle"] += intelligence * 2

    # 2) Questions du Choixpeau : chaque réponse donne +1 à une maison
    for texte, options, maisons_associees in questions:
        # On demande au joueur de choisir une option
        reponse = demander_choix(texte, options)

        # On retrouve l’indice de la réponse choisie
        try:
            indice = options.index(reponse)
        except ValueError:
            # Au cas où (ne devrait pas arriver si demander_choix est bien utilisé)
            print("[Attention] Réponse invalide, la question est ignorée.")
            continue

        maison_choisie = maisons_associees[indice]


        actualiser_points_maison(scores, maison_choisie, 1)


    maison_finale = max(scores, key=scores.get)
    return maison_finale
