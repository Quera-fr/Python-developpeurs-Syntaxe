# Formation : *Python Développeurs – Syntaxe*

Ce dépôt contient l’ensemble des notebooks, scripts et ressources utilisés durant la formation **Python Développeurs – Syntaxe**, organisée sur 3 jours.
L’objectif est d’acquérir les bases solides du langage Python, de comprendre sa logique, ses bibliothèques essentielles et de réaliser des projets concrets autour des API, de la POO et du traitement de données.

---

## Structure du dépôt

```
.
├── J1/
│   ├── 1 Python Programming Introduction.ipynb
│   ├── 2 Fonctions, Modules & Documentation.ipynb
│   └── script.sh
│
├── J2/
│   ├── 3 Bibliothèque Request & FastAPI.ipynb
│   └── 4 Programation Orientée Objet.ipynb
│
└── J3/
    ├── 5 Librairie Numpy.ipynb
    └── 6 Manipulation de CSV.ipynb
```

---

# Programme détaillé

## **Jour 1 — Bases & Syntaxe Python**

*Notebooks :*
`1 Python Programming Introduction.ipynb`
`2 Fonctions, Modules & Documentation.ipynb`

*Contenu :*

* Introduction à Python (syntaxe, types, variables).
* Structures de contrôle : conditions, boucles.
* Fonctions, arguments, exceptions.
* Bibliothèques standards : `os`, `time`…
* Initiation aux modules & documentation.
* Cas pratique : création d’un programme simple.

*Script associé :*
`script.sh`
→ Création d’un environnement virtuel, installation de packages, commandes bash utiles.

---

## **Jour 2 — APIs, Bibliothèques & POO**

*Notebooks :*
`3 Bibliothèque Request & FastAPI.ipynb`
`4 Programation Orientée Objet.ipynb`

*Contenu :*

* Utilisation de `requests` pour consommer des API.
* Découverte & utilisation de **FastAPI** pour créer une API REST documentée.
* Initiation à la Programmation Orientée Objet (POO) :
  classes, attributs, méthodes, héritage.
* Construction de modules et packages Python.

*Cas pratique :*
→ Création d’une API sécurisée et documentée.

---

## **Jour 3 — Data, Numpy & Manipulation de fichiers**

*Notebooks :*
`5 Librairie Numpy.ipynb`
`6 Manipulation de CSV.ipynb`

*Contenu :*

* Gestion des matrices avec **NumPy**.
* Manipulation de fichiers CSV (lecture, écriture).
* Introduction aux workflows data (Pandas, visualisation, etc.).
* Aperçu d’applications concrètes :
  automatisation, scraping, IA, interfaces web.

*Cas pratique :*
→ Création d’un mini-outil d’analyse de données avec Streamlit.

---

# 🚀 Installation & Pré-requis

### 1. Installer Python (recommandé : 3.10+)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Cloner le dépôt

```bash
git clone <votre_repo>
cd <votre_repo>
```

### 3. Exécuter le script d’installation (Jour 1)

```bash
bash J1/script.sh
```

### 4. Lancer un notebook

```bash
jupyter notebook
```

---

# 📚 Bibliothèques utilisées

* **os** – Interaction avec le système d’exploitation.
* **requests** – Consommation d'API HTTP.
* **FastAPI** – Création d’API REST performantes.
* **NumPy** – Calcul scientifique et manipulation matricielle.
* **Pandas** (Jour 3) – Manipulation de données tabulaires.
* **Seaborn / Matplotlib** – Visualisation de données.

---

# 🧑‍🏫 Formateur

**Kévin Duranty** – Formateur Data & Python