from input_utils import demander_texte, demander_nombre
from personnage import initialiser_personnage, afficher_personnage

def introduction():
    print("====== Chapitre 1 : L'arrivée dans le monde magique ======")
    print("Depuis toujours, votre vie ressemble à celle de n'importe qui d'autres.")
    print("Les mêmes rues, les mêmes habitudes... rien qui laisse penser que vous êtes différent(e).")
    print("Et pourtant, quelque chose a toujours semblé... étrange. Comme si vous étiez destiné(e) à autre chose.")
    print("\nTout bascule ce matin-là.")
    print("Un bruit sec résonne à votre fenêtre. Une simple enveloppe... mais scellée d'un blason inconnu.")
    print("Votre aventure commence ici. À vous de découvrir qui vous êtes vraiment.\n")

    input("Appuyez sur Entrée pour ouvrir la lettre...")

def creer_personnage():
    nom = int(input("Entrez le nom de votre personnage :"))
    prenom = int(input("Entrez le prenom de votre personnage :"))
    print("\nAttribuez vos caractéristiques (valeurs entre 1 et 10).")
    courage = demander_nombre("courage : ",1, 10)
    intelligence = demander_nombre("intelligence : ",1, 10)
    loyaute =  demander_nombre("loyauté : ",1, 10)
    ambition = demander_nombre("ambition : ",1, 10)

    attribut = {
        "courage": courage,
        "intelligence": intelligence,
        "layauté": loyaute,
        "ambition": ambition,
    }
    personnage = initialiser_personnage(nom, prenom, attribut)
    print("Voici votre personnage :")
    afficher_personnage(personnage)

    return personnage

