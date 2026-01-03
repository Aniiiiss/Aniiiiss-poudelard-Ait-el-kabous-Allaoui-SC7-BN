import random

from utils.input_utils import load_fichier
from univers.maison import actualiser_points_maison, afficher_maison_gagnante
from univers.personnage import afficher_personnage


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):

    joueurs = list(equipe_data)  # copie

    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": joueurs
    }

    if est_joueur and joueur is not None:
        # On place le joueur en tête de la liste comme Attrapeur
        nouveaux_joueurs = []

        nom_complet = f"{joueur['Prenom']} {joueur['Nom']} (Attrapeur)"
        nouveaux_joueurs.append(nom_complet)

        # On ajoute les autres joueurs en évitant de dupliquer le joueur
        for nom_joueur in joueurs:
            nom_sans_role = nom_joueur.split("(")[0].strip()
            if joueur["Nom"] not in nom_sans_role and joueur["Prenom"] not in nom_sans_role:
                nouveaux_joueurs.append(nom_joueur)

        equipe["joueurs"] = nouveaux_joueurs
        equipe["tirs_joueur"] = 0
        equipe["buts_joueur"] = 0

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):

    proba_but = random.randint(1, 10)

    if joueur_est_joueur and "tirs_joueur" in equipe_attaque:
        equipe_attaque["tirs_joueur"] += 1

    if proba_but >= 6:
        if joueur_est_joueur:
            buteur = equipe_attaque["joueurs"][0]
            if "buts_joueur" in equipe_attaque:
                equipe_attaque["buts_joueur"] += 1
        else:
            buteur = random.choice(equipe_attaque["joueurs"])

        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")
    else:
        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l'attaque !")


def apparition_vifdor():

    valeur = random.randint(1, 6)
    return valeur == 6


def attraper_vifdor(e1, e2):

    gagnante = random.choice([e1, e2])
    gagnante["score"] += 150
    gagnante["attrape_vifdor"] = True
    print(f"Le Vif d'Or a été attrapé par {gagnante['nom']} ! (+150 points)")
    return gagnante


def afficher_score(e1, e2):
    """
    Affiche le score actuel des deux équipes.
    """
    print("Score actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")


def afficher_equipe(maison, equipe):
    """
    Affiche le nom de la maison et la liste des joueurs de l'équipe.
    """
    print(f"Équipe de {maison} :")
    for joueur in equipe["joueurs"]:
        print(f"- {joueur}")
    print()


def match_quidditch(joueur, maisons):
    """
    Gère le déroulement complet d'un match de Quidditch :
    - charge les équipes depuis equipes_quidditch.json
    - crée l'équipe du joueur et l'équipe adverse
    - simule jusqu'à 20 tours ou jusqu'à la capture du Vif d'Or
    - met à jour les points de la maison gagnante (+500 points)
    """
    equipes_data = load_fichier("../data/equipes_quidditch.json")

    maison_joueur = joueur.get("Maison")
    toutes_maisons = list(equipes_data.keys())
    maisons_adverses = [m for m in toutes_maisons if m != maison_joueur]
    maison_adverse = random.choice(maisons_adverses)

    equipe_joueur = creer_equipe(
        maison_joueur,
        equipes_data[maison_joueur],
        est_joueur=True,
        joueur=joueur
    )
    equipe_adverse = creer_equipe(
        maison_adverse,
        equipes_data[maison_adverse],
        est_joueur=False
    )

    print(f"Match de Quidditch : {maison_joueur} vs {maison_adverse} !\n")
    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)

    print(f"Tu joues pour {maison_joueur} en tant qu'Attrapeur.\n")

    equipe_vifdor = None

    for tour in range(1, 21):
        print(f"━━━ Tour {tour} ━━━")

        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)
        tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)

        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            equipe_vifdor = attraper_vifdor(equipe_joueur, equipe_adverse)
            print("Fin du match !")
            afficher_score(equipe_joueur, equipe_adverse)
            break

        input("Appuyez sur Entrée pour continuer...")
        print()

    print("\nRésultat final :")
    afficher_score(equipe_joueur, equipe_adverse)

    score_joueur = equipe_joueur["score"]
    score_adverse = equipe_adverse["score"]

    if score_joueur > score_adverse:
        gagnante = equipe_joueur
        print(f"{equipe_joueur['nom']} remporte le match de Quidditch !")
    elif score_adverse > score_joueur:
        gagnante = equipe_adverse
        print(f"{equipe_adverse['nom']} remporte le match de Quidditch !")
    else:
        gagnante = None
        print("Le match se termine sur un match nul !")

    if equipe_vifdor is not None:
        print(f"Le Vif d'Or a été décisif pour {equipe_vifdor['nom']} !")

    if "tirs_joueur" in equipe_joueur and "buts_joueur" in equipe_joueur:
        print()
        print("Statistiques de ton personnage pendant le match :")
        print(f"- Tirs tentés : {equipe_joueur['tirs_joueur']}")
        print(f"- Buts marqués : {equipe_joueur['buts_joueur']}")

    if gagnante is not None:
        nom_maison_gagnante = gagnante["nom"]
        print()
        print(f"+500 points pour {nom_maison_gagnante} dans la Coupe des Quatre Maisons !")
        actualiser_points_maison(maisons, nom_maison_gagnante, 500)
        print(f"La maison gagnante après ce match est {nom_maison_gagnante} !")
    else:
        print("Aucun point de Coupe n'est attribué en cas de match nul.")


def lancer_chapitre4_quidditch(joueur, maisons):

    print("=== Chapitre 4 : Épreuve de Quidditch ===")
    print("La grande finale de Quidditch s'apprête à commencer...\n")

    match_quidditch(joueur, maisons)

    print()
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain !\n")

    print("Coupe des Quatre Maisons :")
    afficher_maison_gagnante(maisons)
    print()

    print("Profil de ton personnage à la fin de l'aventure :")
    afficher_personnage(joueur)
