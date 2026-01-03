
import random
from utils.input_utils import load_fichier, demander_texte
from maison import ajouter_points_maison, afficher_maison_en_tete
from personnage import afficher_personnage


def apprendre_sorts(joueur, chemin_fichier="../data/sorts.json"):


    def normaliser_sorts(donnees):

        sorts = []

        # Cas 1 : liste de dicts
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
    if "Sortilèges" in joueur and isinstance(joueur["Sortilèges"], list):
        liste_sorts_joueur = joueur["Sortilèges"]
    elif "sortilèges" in joueur and isinstance(joueur["sortilèges"], list):
        liste_sorts_joueur = joueur["sortilèges"]
    else:
        # On choisit une clé "Sortilèges"
        joueur["Sortilèges"] = []
        liste_sorts_joueur = joueur["Sortilèges"]

    quotas = {"Offensif": 1, "Défensif": 1, "Utilitaire": 3}
    appris = []
    deja_appris = set()

    def quotas_restants():
        return quotas["Offensif"] + quotas["Défensif"] + quotas["Utilitaire"]

    # Tirages aléatoires jusqu’à remplir les quotas
    while quotas_restants() > 0:
        sort = random.choice(tous_les_sorts)
        nom = sort["nom"]
        type_ = sort["type"]
        desc = sort["description"]

        # éviter doublons
        if nom in deja_appris:
            continue

        # garder uniquement les types attendus
        if type_ not in quotas:
            continue

        # vérifier quota restant
        if quotas[type_] <= 0:
            continue

        # valider ce sort
        deja_appris.add(nom)
        quotas[type_] -= 1

        # ajout au joueur :
        liste_sorts_joueur.append({"nom": nom, "type": type_, "description": desc})
        appris.append({"nom": nom, "type": type_, "description": desc})

        print(f"Tu viens d'apprendre le sortilège : {nom} ({type_})")
        input("Appuie sur Entrée pour continuer...")

    print("Tu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for s in appris:
        print(f"- {s['nom']} ({s['type']}) : {s['description']}")



def quiz_magie(joueur, chemin_fichier="../data/quiz_magie.json"):

    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.\n")

    donnees = load_fichier(chemin_fichier)

    # Normaliser les questions sous forme de liste de dicts:
    questions = []
    if isinstance(donnees, list):
        for item in donnees:
            if isinstance(item, dict):
                q = item.get("question") or item.get("q")
                r = item.get("reponse") or item.get("réponse") or item.get("answer") or item.get("a")
                if q and r:
                    questions.append({"question": q, "reponse": r})
    elif isinstance(donnees, dict):
        # Cas possible : {"question": "réponse", ...}
        for q, r in donnees.items():
            if isinstance(q, str) and isinstance(r, str):
                questions.append({"question": q, "reponse": r})

    if len(questions) < 4:
        print("Erreur : pas assez de questions dans quiz_magie.json (il en faut au moins 4).")
        return

    # Tirage de 4 questions sans doublons
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

        # Comparaison sans majuscules/minuscules + sans espaces autour
        if rep_joueur.strip().lower() == str(bonne_reponse).strip().lower():
            print("Bonne réponse ! +25 points pour ta maison.\n")
            score += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {bonne_reponse}\n")

    print(f"Score obtenu : {score} points")

    # Ajouter au score global du joueur
    if "score" not in joueur or joueur["score"] is None:
        joueur["score"] = 0
    joueur["score"] += score


def lancer_chapitre_3(personnage, maisons):

    print("\n=== Chapitre 3 : Les cours et la découverte de Poudlard ===\n")

    # 1) Apprentissage des sorts
    apprendre_sorts(personnage, "../data/sorts.json")

    # 2) Quiz magique
    quiz_magie(personnage, "../data/quiz_magie.json")

    # 3) Mise à jour des points de la maison du joueur
    # On suppose que le score du joueur est dans personnage
    score = personnage.get("score", 0)

    # On suppose que le nom de la maison est stocké dans personnage
    maison_joueur = personnage.get("maison") or personnage.get("Maison")

    if maison_joueur is None:
        print(" Maison du joueur introuvable dans le personnage (clé 'maison').")
    else:
        ajouter_points_maison(maisons, maison_joueur, score)

    # 4) Afficher la maison en tête
    afficher_maison_en_tete(maisons)

    # 5) Afficher toutes les informations du joueur
    print("\n=== Profil complet du joueur ===")
    afficher_personnage(personnage)