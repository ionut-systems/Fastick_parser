# Fastick - High-Performance Tick Parser & Analytics UI

Un moteur de traitement de ticks ultra-rapide écrit en **C++**, piloté par une interface graphique moderne en **Python (Tkinter)** et couplé à un module de visualisation de données (**Pandas & Matplotlib**).

## 🚀 Architecture
* **C++ Core** : Moteur d'exécution bas niveau optimisé pour analyser des flux massifs de données de marché en un temps minimal.
* **Python UI** : Interface de contrôle ergonomique permettant de lancer les analyses en un clic, de suivre les logs en temps réel et de générer instantanément des graphiques de performance.

## 🛠️ Fonctionnalités
* Exécution asynchrone du binaire natif via des appels système sécurisés.
* Affichage en temps réel des rapports de performance (temps d'exécution, prix moyen, volume total).
* Visualisation graphique automatisée des ticks pour l'analyse financière.
* Protocole de sortie sécurisé (`[Entrée]`) pour garantir la libération propre des ressources mémoire et graphiques.

## ⚙️ Utilisation
1. Assurez-vous que l'exécutable C++ (`fast_parser.exe`) et le fichier de données (`simulation_ticks.csv`) se trouvent dans le répertoire de travail.
2. Lancez l'interface utilisateur :
   ```bash
   python fastick_ui.py