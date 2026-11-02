# Solveur Automatique d'Équations

## Informations sur le projet

Nom et prénom : BELEBBAYDA Yassine.

Groupe : A1.

## 1. Présentation du projet

Ce projet est réalisé avec le langage Python. Il permet de résoudre des équations en utilisant deux méthodes : la méthode de dichotomie et la méthode de Newton.

Le programme propose trois fonctions différentes. L'utilisateur peut choisir la fonction qu'il veut résoudre.

## 2. Les fonctions utilisées

Le programme contient trois fonctions :

- f(x) = x² - 2
- f(x) = x³ - x - 2
- f(x) = cos(x) - x

Chaque fonction possède aussi sa dérivée pour pouvoir utiliser la méthode de Newton.

## 3. Les méthodes utilisées

### Méthode de dichotomie

Cette méthode consiste à diviser un intervalle en deux parties pour chercher la solution d'une équation.

On continue cette opération jusqu'à obtenir un résultat proche de la solution.

### Méthode de Newton

Cette méthode utilise la fonction et sa dérivée pour trouver une solution.

On commence avec une valeur de départ, puis on calcule de nouvelles valeurs jusqu'à trouver un résultat assez proche de la solution.

## 4. Fonctionnement du programme

Quand on lance le programme :

1. Il affiche les trois fonctions disponibles.
2. L'utilisateur choisit une fonction.
3. Le programme commence par la méthode de Newton.
4. Si Newton ne donne pas de résultat, il essaie la méthode de dichotomie.
5. Il compare ensuite les résultats des deux méthodes.
6. À la fin, il affiche le graphique de la fonction choisie.

## 5. Les bibliothèques utilisées

Dans ce projet, j'ai utilisé :

- `math` : pour utiliser la fonction cosinus et les opérations mathématiques.
- `matplotlib` : pour dessiner les graphiques des fonctions.

## 6. Installation et exécution

Pour utiliser le programme, il faut avoir Python installé.

Installer matplotlib avec cette commande :

```bash
pip install matplotlib
```

Pour lancer le programme :

```bash
python solveur_equations.py
```

## 7. Utilisation de l'IA

J'ai utilisé l'intelligence artificielle comme une aide pendant la réalisation de ce projet, surtout pour corriger les mots et les phrases quand je faisais des erreurs d'écriture.

Elle m'a aidé à améliorer mon texte et à corriger certaines fautes d'orthographe et de grammaire.

## 8. Conclusion

Ce projet m'a permis de pratiquer Python et de découvrir deux méthodes numériques pour résoudre des équations. J'ai aussi appris à utiliser les fonctions, les dérivées et les graphiques en Python.