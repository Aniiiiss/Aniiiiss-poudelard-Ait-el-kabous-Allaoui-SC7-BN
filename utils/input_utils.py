def demande_texte(messsage):
    #Demande un texte à l'utilisateur et s'assure qu'il n'est oas vide
    while True:
        texte = input(messsage)
        texte = texte.strip()
        if texte != '':
            return texte
        else:
            print('Veuillez entrer une texte non vide')


def demande_nombre(message,min_val =None, max_val = None):
    while True:
        saisie = input(message).strip()
        #Verifier si la chaine n'est pas vide
        if saisie =="":
            print("Veuillez entrer un nombre entier.")
            continue

        #Verification du signe négatif
        negatif = False
        if saisie[0] == "-":
            if len(saisie) == 1:
                print("Veuillez entrer un nombre entier.")
                continue
            negatif = True
            chiffres = saisie[1:]
        else:
            chiffres = saisie
        #On verifie que les caracteres sont des chiffres
        if not all("0"<=c<="9"for c in chiffres):
            print("Veuillez entrer un nombre entier.")
            continue
        #On convertie la STR en entier
        valeur = 0
        for c in chiffres:
            valeur = valeur*10 +(ord(c)-ord(0))
        if negatif:
            valeur = valeur*-1
        #Verifier MinvVal
        if min_val is not None and valeur < min_val:
            print("Veuillez entrer un nombre >= à :",min_val)
        #Verifier MaxVal
        if max_val is not None and valeur > max_val:
            print("Veuillez entrer un nombre <=",max_val)
        return valeur