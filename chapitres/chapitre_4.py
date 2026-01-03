from utils.input_utils import demander_choix, load_fichier
from univers.personnage import afficher_personnage, modifier_argent, ajouter_objet
from univers.maison import actualiser_points_maison, afficher_maison_gagnante


def _afficher_titre(titre):

    print("\n" + "=" * 60)
    print(titre)
    print("=" * 60 + "\n")


def evaluation_finale(personnage, maisons):

    _afficher_titre("📘 Examen final de magie")

    maison_joueur = personnage.get("Maison", None)
    if maison_joueur is None:
        print("⚠️ Erreur : aucune maison n’est associée au personnage.")
        return


    questions = load_fichier("../data/examen_final.json")

    score_perso = 0

    for q in questions:
        print(q["enonce"])
        reponse = demander_choix("Choisis une réponse :", q["propositions"])

        if reponse == q["bonne_reponse"]:
            print("✅ Bonne réponse !")
            score_perso += q.get("points_perso", 10)
            actualiser_points_maison(maisons, maison_joueur, q.get("points_maison", 20))
        else:
            print("❌ Mauvaise réponse...")
            score_perso += q.get("points_perso_mauvaise", 0)
            actualiser_points_maison(maisons, maison_joueur, q.get("points_maison_mauvaise", 0))

        print()


    if score_perso > 0:
        print(f"Tu as obtenu {score_perso} points à l’examen.")
        print("Ces points sont convertis en Gallions pour tes prochaines fournitures.")
        modifier_argent(personnage, score_perso)
    else:
        print("Tu n’as obtenu aucun point à l’examen cette fois-ci...")

    print(f"Argent actuel du personnage : {personnage.get('Argent', 0)}")
    input("\n(Appuie sur Entrée pour passer aux évènements de fin d’année...)")


def evenements_fin_annee(personnage, maisons):

    _afficher_titre("🎉 Évènements de fin d’année")

    maison_joueur = personnage.get("Maison", None)
    if maison_joueur is None:
        print("⚠️ Erreur : aucune maison n’est associée au personnage.")
        return

    # Exemple : trois situations possibles
    # Tu peux en ajouter/supprimer facilement.
    # Pas besoin de JSON ici, tout est dans le code.
    # Évènement 1 : farce dans les couloirs
    print("Alors que l’année se termine, une grande farce éclate dans les couloirs.")
    choix1 = demander_choix(
        "Participes-tu à la farce ?",
        [
            "Oui, c’est amusant !",
            "Non, je préfère éviter les ennuis.",
            "Je dénonce discrètement la farce aux préfets."
        ]
    )

    if choix1 == "Oui, c’est amusant !":
        print("Les élèves de ta maison rient beaucoup, mais les professeurs un peu moins...")
        actualiser_points_maison(maisons, maison_joueur, -10)
        print(f"Ta maison perd 10 points.")
    elif choix1 == "Non, je préfère éviter les ennuis.":
        print("Tu restes à l’écart et évites les problèmes.")
        actualiser_points_maison(maisons, maison_joueur, 5)
        print(f"Ta maison gagne 5 points.")
    else:
        print("Les professeurs apprécient ton sens des responsabilités.")
        actualiser_points_maison(maisons, maison_joueur, 15)
        print(f"Ta maison gagne 15 points.")

    print()

    # Évènement 2 : aide en bibliothèque
    print("La bibliothécaire cherche de l’aide pour ranger des grimoires poussiéreux.")
    choix2 = demander_choix(
        "Que fais-tu ?",
        [
            "Tu proposes ton aide.",
            "Tu fais semblant de ne pas entendre.",
            "Tu envoies quelqu’un d’autre à ta place."
        ]
    )

    if choix2 == "Tu proposes ton aide.":
        print("Tu passes un long moment à ranger les rayons.")
        actualiser_points_maison(maisons, maison_joueur, 10)
        ajouter_objet(personnage, "Inventaire", "Marque-page magique")
        print("Ta maison gagne 10 points et tu obtiens un 'Marque-page magique'.")
    elif choix2 == "Tu fais semblant de ne pas entendre.":
        print("Personne ne remarque vraiment ton absence.")
        print("Aucun point n’est gagné ni perdu.")
    else:
        print("Le professeur découvre vite la supercherie.")
        actualiser_points_maison(maisons, maison_joueur, -5)
        print("Ta maison perd 5 points.")

    print()

    # Évènement 3 : match de Quidditch
    print("Un dernier match de Quidditch amical est organisé entre les maisons.")
    choix3 = demander_choix(
        "Quel rôle joues-tu dans ce match ?",
        [
            "Attrapeur pour ta maison.",
            "Supporter dans les tribunes.",
            "Tu révises à la bibliothèque à la place."
        ]
    )

    if choix3 == "Attrapeur pour ta maison.":
        print("Tu attrapes le Vif d’Or au dernier moment !")
        actualiser_points_maison(maisons, maison_joueur, 30)
        print("Ta maison gagne 30 points.")
    elif choix3 == "Supporter dans les tribunes.":
        print("Tu encourages ton équipe avec enthousiasme.")
        actualiser_points_maison(maisons, maison_joueur, 10)
        print("Ta maison gagne 10 points.")
    else:
        print("Tu n’assistes pas au match, mais tu es prêt pour les examens futurs.")
        print("Aucun point n’est gagné ni perdu.")

    input("\n(Appuie sur Entrée pour voir le bilan de l’année...)")


def bilan_final(personnage, maisons):

    _afficher_titre(" Bilan de fin d’année")

    print("Voici l’état final de ton personnage :\n")
    afficher_personnage(personnage)

    print("\nPoints des maisons :")
    for nom_maison, points in maisons.items():
        print(f"- {nom_maison} : {points} points")

    print()
    afficher_maison_gagnante(maisons)

    input("\n(Appuie sur Entrée pour conclure l’année à Poudlard...)")


def lancer_chapitre_4(personnage, maisons):

    _afficher_titre("📖 Chapitre 4 – Fin d’année à Poudlard")

    evaluation_finale(personnage, maisons)
    evenements_fin_annee(personnage, maisons)
    bilan_final(personnage, maisons)

    print("\n Fin de l’aventure pour cette année à Poudlard !")
