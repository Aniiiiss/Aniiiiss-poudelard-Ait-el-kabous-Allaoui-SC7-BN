import random

from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison, afficher_maison_gagnante


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": []
    }

    joueurs_base = []
    if isinstance(equipe_data, dict) and "joueurs" in equipe_data:
        joueurs_base = equipe_data["joueurs"]
    elif isinstance(equipe_data, list):
        joueurs_base = equipe_data

    if not isinstance(joueurs_base, list):
        joueurs_base = []

    if est_joueur and joueur is not None:
        nom_j = str(joueur.get("Prenom", "")).strip()
        prenom_j = str(joueur.get("Nom", "")).strip()
        nom_complet = (nom_j + " " + prenom_j).strip()
        if nom_complet == "":
            nom_complet = "Joueur"
        equipe["joueurs"].append(nom_complet + " (Attrapeur)")

        for p in joueurs_base:
            if isinstance(p, str):
                if nom_complet.lower() not in p.lower():
                    equipe["joueurs"].append(p)
            else:
                equipe["joueurs"].append(str(p))
    else:
        for p in joueurs_base:
            if isinstance(p, str):
                equipe["joueurs"].append(p)
            else:
                equipe["joueurs"].append(str(p))

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)

    if proba_but >= 6:
        buteur = ""
        if joueur_est_joueur and len(equipe_attaque["joueurs"]) > 0:
            buteur = equipe_attaque["joueurs"][0]
        else:
            if len(equipe_attaque["joueurs"]) > 0:
                buteur = random.choice(equipe_attaque["joueurs"])
            else:
                buteur = "Un joueur"

        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
        print(buteur + " marque un but pour " + equipe_attaque["nom"] + " ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] += 1
        print(equipe_defense["nom"] + " bloque l’attaque !")


def apparition_vifdor():
    return random.randint(1, 6) == 6


def attraper_vifdor(e1, e2):
    gagnant = random.choice([e1, e2])
    gagnant["score"] += 150
    gagnant["attrape_vifdor"] = True
    print("\nLe Vif d’Or a été attrapé par " + gagnant["nom"] + " ! (+150 points)\n")
    return gagnant


def afficher_score(e1, e2):
    print("\nScore actuel :")
    print("→ " + e1["nom"] + " : " + str(e1["score"]) + " points")
    print("→ " + e2["nom"] + " : " + str(e2["score"]) + " points\n")


def afficher_equipe(maison, equipe):
    print("Équipe de " + maison + " :")
    for j in equipe.get("joueurs", []):
        print(" - " + str(j))
    print("")


def match_quidditch(joueur, maisons):
    data = load_fichier("data/equipes_quidditch.json")

    maison_joueur = joueur.get("Maison", None)
    if maison_joueur is None or str(maison_joueur).strip() == "":
        print("Erreur : le joueur n’a pas de maison. Chapitre 2 requis.")
        return

    if not isinstance(data, dict) or maison_joueur not in data:
        print("Erreur : données Quidditch invalides ou maison introuvable dans le JSON.")
        return

    maisons_possibles = []
    for m in data.keys():
        if m != maison_joueur:
            maisons_possibles.append(m)

    if len(maisons_possibles) == 0:
        print("Erreur : aucune maison adverse disponible.")
        return

    maison_adverse = random.choice(maisons_possibles)

    e1 = creer_equipe(maison_joueur, data[maison_joueur], est_joueur=True, joueur=joueur)
    e2 = creer_equipe(maison_adverse, data[maison_adverse], est_joueur=False, joueur=None)

    print("\nMatch de Quidditch : " + e1["nom"] + " vs " + e2["nom"] + " !\n")
    afficher_equipe(e1["nom"], e1)
    afficher_equipe(e2["nom"], e2)

    print("Tu joues pour " + e1["nom"] + " en tant qu’Attrapeur\n")

    for tour in range(1, 21):
        print("━━━ Tour " + str(tour) + " ━━━\n")

        tentative_marque(e2, e1, joueur_est_joueur=False)
        tentative_marque(e1, e2, joueur_est_joueur=True)

        afficher_score(e1, e2)

        if apparition_vifdor():
            attraper_vifdor(e1, e2)
            break

        input("Appuyez sur Entrée pour continuer... ")
        print("")

    print("Fin du match !")
    afficher_score(e1, e2)

    if e1["score"] > e2["score"]:
        print("Résultat final : " + e1["nom"] + " remporte le match !")
        actualiser_points_maison(maisons, e1["nom"], 500)
    elif e2["score"] > e1["score"]:
        print("Résultat final : " + e2["nom"] + " remporte le match !")
        actualiser_points_maison(maisons, e2["nom"], 500)
    else:
        print("Résultat final : match nul ! Aucun bonus de victoire.")

    afficher_maison_gagnante(maisons)


def lancer_chapitre4_quidditch(joueur, maisons):
    print("\n============================================================")
    print("🏟️ Chapitre 4 – Épreuve de Quidditch")
    print("============================================================\n")

    match_quidditch(joueur, maisons)

    print("\nFin du Chapitre 4 — Quelle performance incroyable sur le terrain !\n")
    print("Coupe des Quatre Maisons — Classement actuel :")
    afficher_maison_gagnante(maisons)