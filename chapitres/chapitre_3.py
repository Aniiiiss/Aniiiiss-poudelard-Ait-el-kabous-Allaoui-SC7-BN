import random

from utils.input_utils import load_fichier, demander_texte
from univers.maison import actualiser_points_maison, afficher_maison_gagnante
from univers.personnage import afficher_personnage


def apprendre_sorts(joueur, chemin_fichier="data/sorts.json"):

    def normaliser_sorts(donnees):
        sorts = []

        # Cas 1 : liste de dict
        if isinstance(donnees, list):
            for s in donnees:
                if not isinstance(s, dict):
                    continue
                nom = s.get("nom") or s.get("name")
                type_ = s.get("type") or s.get("categorie") or s.get("category")
                desc = s.get("description") or s.get("desc")
                if nom and type_ and desc:
                    sorts.append({"nom": nom, "type": type_, "description": desc})

        # Cas 2 : dict { "Obliviate": {"type":..., "description":...}, ... }
        elif isinstance(donnees, dict):
            for nom, info in donnees.items():
                if not isinstance(info, dict):
                    continue
                type_ = info.get("type") or info.get("categorie") or info.get("category")
                desc = info.get("description") or info.get("desc")
                if nom and type_ and desc:
                    sorts.append({"nom": nom, "type": type_, "description": desc})

        return sorts

    print("Tu commences tes cours de magie à Poudlard...")

    donnees = load_fichier(chemin_fichier)
    tous_les_sorts = normaliser_sorts(donnees)

    if not tous_les_sorts:
        print("Erreur : aucun sort valide trouvé dans le fichier de sorts.")
        return

    # S'assurer que la liste des sortilèges existe
    if "Sortilèges" not in joueur or not isinstance(joueur["Sortilèges"], list):
        joueur["Sortilèges"] = []
    liste_sorts_joueur = joueur["Sortilèges"]

    quotas = {"Offensif": 1, "Défensif": 1, "Utilitaire": 3}
    appris = []
    deja_appris = set()

    def quotas_restants():
        return quotas["Offensif"] + quotas["Défensif"] + quotas["Utilitaire"]

    while quotas_restants() > 0:
        sort = random.choice(tous_les_sorts)
        nom = sort["nom"]
        type_ = sort["type"]
        desc = sort["description"]

        if nom in deja_appris:
            continue
        if type_ not in quotas:
            continue
        if quotas[type_] <= 0:
            continue

        deja_appris.add(nom)
        quotas[type_] -= 1

        liste_sorts_joueur.append({"nom": nom, "type": type_, "description": desc})
        appris.append({"nom": nom, "type": type_, "description": desc})

        print(f"Tu viens d'apprendre le sortilège : {nom} ({type_})")
        input("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for s in appris:
        print(f"- {s['nom']} ({s['type']}) : {s['description']}")


def quiz_magie(joueur, chemin_fichier="data/quiz_magie.json"):

    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")

    donnees = load_fichier(chemin_fichier)

    questions = []
    if isinstance(donnees, list):
        for item in donnees:
            if isinstance(item, dict):
                q = item.get("question") or item.get("q")
                r = item.get("reponse") or item.get("réponse") or item.get("answer") or item.get("a")
                if q and r:
                    questions.append({"question": q, "reponse": r})
    elif isinstance(donnees, dict):
        for q, r in donnees.items():
            if isinstance(q, str) and isinstance(r, str):
                questions.append({"question": q, "reponse": r})

    if len(questions) < 4:
        print("Erreur : pas assez de questions dans quiz_magie.json (il en faut au moins 4).")
        return 0

    tirage = []
    while len(tirage) < 4:
        q = random.choice(questions)
        if q not in tirage:
            tirage.append(q)

    score = 0

    for i in range(4):
        question = tirage[i]["question"]
        bonne_reponse = tirage[i]["reponse"]

        print(f"{i + 1}. {question}")
        rep_joueur = demander_texte("> ")

        if rep_joueur.strip().lower() == str(bonne_reponse).strip().lower():
            print("Bonne réponse ! +25 points pour ta maison.\n")
            score += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {bonne_reponse}\n")

    print(f"Score obtenu : {score} points")

    if "score" not in joueur or joueur["score"] is None:
        joueur["score"] = 0
    joueur["score"] += score

    return score


def lancer_chapitre_3(personnage, maisons):

    print("\n=== Chapitre 3 : Les cours et la découverte de Poudlard ===\n")

    apprendre_sorts(personnage)
    score = quiz_magie(personnage)

    maison_joueur = personnage.get("Maison") or personnage.get("maison")

    if maison_joueur is None:
        print("️ Maison du joueur introuvable dans le personnage (clé 'Maison').")
    else:
        actualiser_points_maison(maisons, maison_joueur, score)

    afficher_maison_gagnante(maisons)

    print("\n=== Profil complet du joueur ===")
    afficher_personnage(personnage)
