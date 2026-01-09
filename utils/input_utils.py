import json


def demander_texte(message):
    while True:
        saisie = input(message).strip()
        if saisie == "":
            print("Veuillez entrer du texte (pas vide).")
        else:
            return saisie


def demander_nombre(message, mini, maxi):
    while True:
        s = input(message).strip()
        if s == "":
            print("Veuillez entrer un nombre entier.")
            continue

        negatif = False
        if s[0] == "-":
            if len(s) == 1:
                print("Veuillez entrer un nombre entier.")
                continue
            negatif = True
            s = s[1:]

        ok = True
        for c in s:
            if not ("0" <= c <= "9"):
                ok = False
                break

        if not ok:
            print("Veuillez entrer un nombre entier.")
            continue

        valeur = 0
        for c in s:
            valeur = valeur * 10 + (ord(c) - ord("0"))

        if negatif:
            valeur = -valeur

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
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)
