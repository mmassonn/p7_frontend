# Analyse de sentiments grâce au DeepLearning

## Description

Chaque jour, 500 millions de tweets sont publiés. Parmi eux, certains peuvent déclencher de véritables crises pour les entreprises.
Pour anticiper et gérer ces situations, il est essentiel de comprendre les sentiments exprimés sur les réseaux sociaux. 
Dans ce répertoire, je met en place l'interface Streamlit comme Frontend. Elle interagit avec l'application Microsoft Azure lequel
un modèle XGBoost réalise les prédictions.

## Installation

* **Prérequis:** projet réalisé avec python 3.12
* **Installation des dépendances:** `pip install -r requirements.txt`
* **Interface:** Interface via interface.py sur le service Streamlit via le répertoire .devcontainer.

## Utilisation

Ce projet a été développé à des fins pédagogiques, dans le cadre de ma formation chez OpenClassrooms. 
Il n'est pas destiné à une utilisation en production. Vous ne pouvez pas l'utiliser telquel car le modèle est stocké 
sur un serveur sécurisé.
