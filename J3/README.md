# Projet : Interface de data app avec Streamlit

L’objectif de cet exercice est de créer une application **Streamlit** avec deux fonctionnalités principales :

1. **Manipulation et visualisation de CSV**
2. **Collecte (scraping) d’articles du site *Les Échos* à partir d’un mot-clé**

---

## 🎯 Objectifs pédagogiques

* Découvrir ou consolider l’utilisation de **Streamlit** pour créer une interface web simple.
* Manipuler des données avec **pandas**.
* Générer des visualisations interactives.
* Mettre en place un petit **scraper** piloté depuis une interface graphique.

---

## **Partie 1 – Interface CSV : upload → édition → graphiques → téléchargement**

Créer dans Streamlit une section `DataProcess` qui permet de :

1. **Verser un fichier CSV**

   * Utiliser `st.file_uploader` pour charger un fichier `.csv`.
   * Lire le fichier avec `pandas.read_csv`.

2. **Afficher et éditer les données**

   * Afficher le DataFrame avec `st.dataframe` ou `st.data_editor` (Streamlit ≥ 1.22 permet l’édition).
   * L’utilisateur doit pouvoir **modifier les valeurs** directement depuis le front (si vous utilisez `st.data_editor`, récupérer le DataFrame modifié).

3. **Sélectionner les colonnes pour les graphiques**

   * Proposer un ou plusieurs widgets pour choisir :

     * Une colonne pour l’axe X
     * Une ou plusieurs colonnes numériques pour l’axe Y
   * Générer un graphique (ex. `st.line_chart`, `st.bar_chart` ou un graphique custom via `matplotlib` ou `plotly`).

4. **Télécharger le CSV modifié**

   * Permettre le téléchargement du DataFrame (après édition) au format `.csv` via `st.download_button`.

-> **Attendu Partie 1**

* Une interface simple, lisible, qui permet réellement :

  * d’uploader un CSV
  * d’éditer des données
  * de visualiser des graphiques en fonction de colonnes choisies
  * de récupérer le fichier modifié en téléchargement

---

## **Partie 2 – Collecte d’articles *Les Échos* dans un CSV**

Créer une deuxième section Streamlit (par exemple `st.header("Scraping Les Échos")`) qui permet :

1. **Saisie d’un mot-clé**

   * Un champ de texte (`st.text_input`) dans lequel l’utilisateur tape un mot-clé (ex : “inflation”, “immobilier”, “IA”, etc.).

2. **Bouton de lancement du scraping**

   * Un bouton `st.button("Lancer la recherche")` ou équivalent.
   * Au clic, lancer une fonction Python qui :

     * construit l’URL de recherche sur **Les Échos** (en fonction du mot-clé),
     * envoie une ou plusieurs requêtes HTTP,
     * extrait pour chaque article au minimum :

       * le **titre**
       * l’**URL**
       * éventuellement un **chapeau / résumé**
       * la **date** si disponible

3. **Affichage des résultats**

   * Afficher les résultats dans un DataFrame `pandas` dans l’interface Streamlit.

4. **Export en CSV**

   * Permettre de **télécharger** les résultats dans un fichier CSV (via `st.download_button`).

⚠️ **Remarque importante**

* Respecter les règles d’utilisation du site (*robots.txt*, conditions générales, etc.).
* Cet exercice est pédagogique : adapter le scraping en respectant le cadre légal et éthique.

-> **Attendus Partie 2**

* Une interface où l’utilisateur :

  * saisit un mot-clé
  * déclenche la recherche
  * voit une liste d’articles structurée
  * peut télécharger ces résultats au format CSV
