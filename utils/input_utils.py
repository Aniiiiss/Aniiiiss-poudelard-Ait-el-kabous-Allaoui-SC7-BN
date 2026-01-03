import json


def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte != "":
            return texte
        print("Veuillez entrer un texte non vide.")


def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()

        if saisie == "":
            print("Veuillez entrer un nombre entier.")
            continue

        negatif = False
        if saisie[0] == "-":
            if len(saisie) == 1:
                print("Veuillez entrer un nombre entier.")
                continue
            negatif = True
            chiffres = saisie[1:]
        else:
            chiffres = saisie

        for c in chiffres:
            if c < "0" or c > "9":
                print("Veuillez entrer un nombre entier.")
                break
        else:
            valeur = 0
            for c in chiffres:
                valeur = valeur * 10 + (ord(c) - ord("0"))

            if negatif:
                valeur = -valeur

            if min_val is not None and valeur < min_val:
                print(f"Veuillez entrer un nombre >= {min_val}.")
                continue

            if max_val is not None and valeur > max_val:
                print(f"Veuillez entrer un nombre <= {max_val}.")
                continue

            return valeur


def demander_choix(message, options):
    print(message)
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    choix = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix - 1]


def load_fichier(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as f:
        return json.load(f)
