# univers/personnage.py

def initialiser_personnage(nom, prenom, attributs):

    personnage = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,          # argent de départ défini dans l'énoncé
        "Inventaire": [],       # liste des objets possédés
        "Sortilèges": [],       # liste des sorts connus
        "Attributs": attributs  # dictionnaire des attributs
    }
    return personnage


def afficher_personnage(joueur):

    print("Profil du personnage :")
    print(f"Nom : {joueur.get('Nom', 'Inconnu')}")
    print(f"Prenom : {joueur.get('Prenom', 'Inconnu')}")
    print(f"Argent : {joueur.get('Argent', 0)}")

    # Inventaire
    inventaire = joueur.get("Inventaire", [])
    if inventaire:
        objets_str = ", ".join(str(obj) for obj in inventaire)
    else:
        objets_str = ""
    print(f"Inventaire : {objets_str}")

    # Sortilèges
    sortileges = joueur.get("Sortilèges", [])
    if sortileges:
        sortileges_str = ", ".join(str(s) for s in sortileges)
    else:
        sortileges_str = ""
    print(f"Sortilèges : {sortileges_str}")

    attributs = joueur.get("Attributs", {})
    print("Attributs :")
    for nom_attr, valeur in attributs.items():
        print(f" - {nom_attr} : {valeur}")


def modifier_argent(joueur, montant):

    argent_actuel = joueur.get("Argent", 0)
    nouvel_argent = argent_actuel + montant

    # On évite les valeurs négatives
    if nouvel_argent < 0:
        nouvel_argent = 0

    joueur["Argent"] = nouvel_argent


def ajouter_objet(joueur, cle, objet):

    if cle not in joueur:
        joueur[cle] = []

    # On vérifie que c’est bien une liste
    if not isinstance(joueur[cle], list):
        raise TypeError(f"La valeur associée à la clé '{cle}' doit être une liste.")

    # On ajoute l’objet (converti en chaîne au cas où)
    joueur[cle].append(str(objet))
