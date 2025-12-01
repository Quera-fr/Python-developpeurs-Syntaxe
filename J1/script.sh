# Installation de python
sudo apt install python3
sudo apt install python3-pip



# Vérifier la version installée de Python
python --version
python -V

# Lancer l'interpréteur Python interactif
python

# Exécuter un script Python
python mon_script.py

# Installer un module (exemple : requests)
pip install requests

# Mettre à jour pip (gestionnaire de paquets Python)
python -m pip install --upgrade pip

# Vérifier la liste des paquets installés
pip list

# Rechercher de l’aide sur une commande pip
pip help

# Afficher les informations sur un module installé
pip show 'nom-du-module'

# Créer un environnement virtuel (isolé pour un projet)
python -m venv env

# Activer l’environnement virtuel
# Sous Windows
env\Scripts\activate
# Sous macOS/Linux
source env/bin/activate

# Désactiver l’environnement virtuel
deactivate

#Mettre à jour un module
pip install --upgrade requests

# Afficher la documentation d'une fonction (exemple : print)
python -c "help(print)"


# Supprimer un module
pip uninstall requests

# Exécuter un script Python avec des arguments
python mon_script.py arg1 arg2