# Projet Python Poudlard (TI101)

Jeu narratif en console inspiré de l’univers de Harry Potter.  
Le joueur crée son personnage, progresse à travers plusieurs chapitres (arrivée dans le monde magique, répartition dans une maison, apprentissage de sorts, quiz, fin d’année) et une extension (Chapitre 5).

## Auteurs
- Anis Ait el Kabous
- Anas Allaoui

## Prérequis
- Python 3.10+ 
- Aucune dépendance externe (bibliothèque standard uniquement)

## Journal de bord

Période couverte : du 30 novembre 2025 au 28 décembre 2025 (d’après le graphique GitHub).  
Binôme : Anis Ait el Kabous (Aniiiss) et Anas Allaoui (Fluox-Anas).

### Semaine du 30 novembre au 6 décembre 2025 — Mise en place et architecture
- Objectif : démarrer proprement le projet et préparer le travail en binôme.
- Travail réalisé :
  - création de l’architecture globale du projet (dossiers `chapitres/`, `univers/`, `utils/`, `data/`) ;
  - création des fichiers de base (ex. `main.py`, `menu.py`, fichiers chapitres, modules univers) ;
  - ajout des fichiers JSON dans `data/`.
- Répartition :
  - Anis : mise en place de l’architecture (arborescence, création des fichiers à prévoir).
  - Anas : mise en place parallèle et premiers tests d’intégration.
- Fin de semaine :
  - répartition définitive du travail sur le code pour la suite :
    - Anis : `utils/`, chapitres 1, 3 et 5
    - Anas : le reste (chapitres 2 et 4 + modules associés + intégration)

### Semaine du 7 au 13 décembre 2025 — Développement des bases
- Objectif : avancer sur les modules attribués à chacun.
- Travail réalisé :
  - Anis :
    - implémentation du dossier `utils` (fonctions de saisie + chargement JSON) ;
    - démarrage/avancement du Chapitre 1 (début de l’aventure, création du personnage, séquences d’introduction).
  - Anas :
    - développement des chapitres et modules qui lui sont attribués (parties restantes du scénario et logique associée) ;
    - premiers enchaînements entre les modules.
- Problèmes rencontrés (classiques sur ce type de projet) :
  - ajustements d’imports entre modules et cohérence des chemins vers `data/`.
- Solutions :
  - standardisation des imports (ex. `univers/...`, `utils/...`) et utilisation de chemins `data/...`.

### Semaine du 14 au 20 décembre 2025 — Consolidation et préparation du rendu intermédiaire
- Objectif : stabiliser l’enchaînement des chapitres et corriger les bugs.
- Travail réalisé :
  - correction de bugs (imports, saisies, chemins de fichiers) ;
  - harmonisation des structures de données partagées (dictionnaire personnage, dictionnaire maisons) ;
  - tests d’exécution de l’aventure jusqu’au chapitre 3.

### 21 décembre 2025 — Dépôt intermédiaire
- Objectif : rendre une version fonctionnelle du projet.
- Résultat : dépôt intermédiaire validé avec une aventure jouable jusqu’au Chapitre 3.

### Semaine du 22 au 27 décembre 2025 — Pause et conception du Chapitre 5 (extension)
- Objectif : imaginer une extension originale pour se différencier.
- Travail réalisé :
  - réflexion et conception du scénario du Chapitre 5 (extension) ;
  - choix d’une approche originale : gestion d’une boutique (mini-jeu de gestion/économie).

### Semaine du 28 décembre 2025 — Finalisation et ajustements en collaboration directe
- Objectif : finaliser le projet et stabiliser la version finale.
- Travail réalisé :
  - Anis :
    - développement du Chapitre 5 (boutique) ;
    - finalisation des chapitres dont il est responsable (1, 3, 5) et du dossier `utils`.
  - Anas :
    - finalisation des chapitres restants (2 et 4) et des modules associés ;
    - intégration et tests avec le menu.
  - Collaboration directe :
    - derniers ajustements ensemble (corrections finales, cohérence des messages, intégration complète dans `menu.py`, tests de lancement via `main.py`).

### Répartition finale du travail
- Anis Ait el Kabous : dossier `utils`, Chapitre 1, Chapitre 3, Chapitre 5.
- Anas Allaoui : Chapitre 2, Chapitre 4, modules associés et intégration globale.
- Finalisation : ajustements finaux réalisés ensemble lors de la dernière journée.


## Lancer le jeu
À la racine du projet :

```bash
python main.py
