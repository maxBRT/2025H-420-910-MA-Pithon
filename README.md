# 🐍 Pithon - Interpréteur Python Académique

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)

> **Pithon** est un interpréteur Python conçu dans un cadre académique pour comprendre les mécanismes internes des langages de programmation. Une expérience d'apprentissage complète pour explorer la théorie des langages et l'implémentation d'interpréteurs.

## 🎓 Objectifs Pédagogiques

Ce projet académique vise à :

### 📚 **Apprentissage Théorique**
- Comprendre les concepts fondamentaux de la théorie des langages
- Explorer les phases de compilation : lexing, parsing, évaluation
- Maîtriser les arbres syntaxiques abstraits (AST) et leur manipulation

### 🔬 **Expérimentation Pratique**
- Implémenter un interpréteur complet de A à Z
- Tester différentes stratégies d'évaluation
- Comparer avec l'interpréteur Python officiel

## ✨ Fonctionnalités Implémentées

### 🧠 **Concepts Fondamentaux**
- **Types de données** : Nombres, booléens, chaînes, listes, tuples, None
- **Structures de contrôle** : if/else, while, for, break, continue
- **Fonctions** : Définition, appel, arguments variables, récursion
- **Classes et objets** : Programmation orientée objet complète
- **Opérateurs** : Arithmétiques, logiques, de comparaison, d'appartenance

### 🛠️ **Outils d'Exploration**
- **CLI interactif** : Interface pour tester et expérimenter
- **Mode AST** : Visualisation de l'arbre syntaxique abstrait
- **Tests automatisés** : Suite de tests complète avec 50+ cas d'usage
- **Gestion d'erreurs** : Messages d'erreur éducatifs et informatifs

## 🚀 Installation Rapide

### Prérequis
- Python 3.10 ou supérieur
- Gestionnaire de paquets `uv` (recommandé)

### Installation
```bash
# Cloner le repository
git clone 
cd pithon

# Installer avec uv (recommandé)
uv sync

```

## 🎮 Expérimentation et Apprentissage

### Interface Interactive
```bash
# Lancer l'interpréteur pour expérimenter
uv run pithon

# Mode AST pour comprendre la structure syntaxique
uv run pithon --ast
```

### Exécution de Fichiers
```bash
# Exécuter un programme Python pour voir l'interpréteur en action
uv run pithon mon_programme.py

# Visualiser l'AST pour comprendre le parsing
uv run pithon --ast mon_programme.py
```

### Tests et Validation
```bash
# Lancer la suite de tests pour vérifier les concepts
uv run pytest
```

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

## 🙏 Remerciements

- **Vincent Archambault** ([@archambaultv-prof](https://github.com/archambaultv-prof)) - Pour son encadrement, ses conseils avisés et son soutien tout au long de ce projet.