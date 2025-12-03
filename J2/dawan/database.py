import sqlite3

class DataBase:
    """
    Classe permettant d'interagir avec une base de données SQLite.

    Cette classe fournit des méthodes pour se connecter à une base de données,
    créer des tables, insérer des données et récupérer des informations.
    """

    def __init__(self, name:str='database') -> None:
        """
        Initialise une nouvelle instance de la classe DataBase.

        Args:
            name (str, optional): Le nom de la base de données. Le fichier aura l'extension '.db'.
        """
        self.name = name

    def open(self) -> tuple:
        """
        Ouvre une connexion à la base de données et crée un curseur.

        Si la base de données n'existe pas, elle sera créée.

        Returns:
            tuple: Un tuple contenant le curseur et l'objet de connexion (self.curs, self.conn).
        """
        self.conn = sqlite3.connect(self.name+'.db')
        self.curs = self.conn.cursor()
        return self.curs, self.conn

    def create_table(self, table:str, **kwargs) -> None:
        """
        Crée une table dans la base de données.

        Args:
            table (str): Le nom de la table à créer.
            **kwargs: Les noms des colonnes de la table avec leurs types.
                      Ex: `create_table('users', name='TEXT', age='INTEGER')`
        """
        # Ouverture de la connexion
        self.curs, self.conn = self.open()

        # Liste des colonnes de la table
        colunms = str(kwargs).replace('{', '').replace('}', '').replace(':', '').replace("'", '')
        
        # Commande SQL
        prompt = f"CREATE TABLE IF NOT EXISTS {table} (id INTEGER PRIMARY KEY, {colunms})"
        self.curs.execute(prompt)

        # Fermeture de la connexion
        self.conn.close()


    def insert_to_table(self, table:str, **kwargs) -> None:
        """
        Insère une ligne de données dans une table spécifiée.

        Args:
            table (str): Le nom de la table dans laquelle insérer les données.
            **kwargs: Les noms des colonnes et leurs valeurs à insérer.
                      Ex: `insert_to_table('users', name='Alice', age=30)`
        """
        # Ouverture de la connexion
        self.curs, self.conn = self.open()

        # Création de la commande SQL
        columns = str(tuple(kwargs.keys()))
        values = str(tuple(kwargs.values()))

        prompt = f"INSERT INTO {table} {columns} VALUES {values}"

        # Exécution de la commande SQL
        self.curs.execute(prompt)
        self.conn.commit()

        # Fermeture de la connexion
        self.conn.close()
        print(f'Les données ont été ajoutées à la table {table}.')


    def show_table(self, table:str) -> list:
        """
        Récupère toutes les lignes d'une table spécifiée.

        Args:
            table (str): Le nom de la table à afficher.

        Returns:
            list: Une liste de tuples, où chaque tuple représente une ligne de la table.
                  Retourne une liste vide si la table est vide ou en cas d'erreur.
        
        """
        self.curs, self.conn = self.open()
        self.curs.execute(f'SELECT * FROM {table}')
        return self.curs.fetchall()