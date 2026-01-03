import json


def demander_texte(message):

    while True:
        saisie = input(message)
        saisie = saisie.strip()

        if saisie == "":
            print("Veuillez entrer du texte (pas vide).")
        else:
            return saisie


def demander_nombre(message, mini, maxi):
  "
    while True:
        saisie = input(message)
        saisie = saisie.strip()

        # vide ?
        if saisie == "":
            print("Veuillez entrer un nombre entier.")
            continue

        # signe négatif ?
        negatif = False
        if saisie[0] == "-":
            if len(saisie) == 1:
                print("Veuillez entrer un nombre entier.")
                continue
            negatif = True
            chiffres = saisie[1:]
        else:
            chiffres = saisie

        # vérifier que tous les caractères sont des chiffres
        ok = True
        for c in chiffres:
            if not ("0" <= c <= "9"):
                ok = False
                break

        if not ok:
            print("Veuillez entrer un nombre entier.")
            continue

        # conversion manuelle str -> int
        valeur = 0
        for c in chiffres:
            valeur = valeur * 10 + (ord(c) - ord("0"))

        if negatif:
            valeur = -valeur

        # vérifier les bornes
        if valeur < mini or valeur > maxi:
            print(f"Veuillez entrer un nombre entre {mini} et {maxi}.")
            continue

        return valeur


def demander_choix(message, options):

    print(message)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    choix = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix - 1]


def load_fichier(chemin):

    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Erreur : fichier introuvable : {chemin}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Erreur : fichier JSON invalide : {chemin}")
        exit(1)