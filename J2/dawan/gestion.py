import time, os, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_article(text_input:str='Python') -> None:
    """
    Fonction qui retourne dans un json les articles du site lesechos.fr


    Parametres
    -----
    text_input : str | Objet de la recherche sur le site les echos.


    Return
    ------
    None
    """

    # Ouverture du navigateur
    driver = webdriver.Chrome()

    # Chargement du site lesechos.fr
    driver.get('https://www.lesechos.fr/')

    # Accepter les cookies
    driver.find_element(By.CLASS_NAME, 'inv-cmp-button.inv-font-btn.inv-bold.inv-mb_16').click()

    # Champ de recherche
    driver.find_element(By.CLASS_NAME,'sc-nmm9yg-0 sc-1wngykz-0 exMYHO MjauK sc-qhazat-0 jJgOCM'.replace(' ', '.')).click()

    time.sleep(3)

    # Recherche
    driver.find_element(By.CLASS_NAME, 'text-field__input').send_keys(text_input + Keys.ENTER)

    time.sleep(3)

    # Liste des articles
    articles = driver.find_elements(By.TAG_NAME, 'article')

    # Affichage des titre et des images
    for article in articles:
        print(article.find_element(By.TAG_NAME, 'h3').text)
        print(article.find_element(By.TAG_NAME, 'img').get_attribute('src'))

    # Fermeture du navigateur
    driver.close()


def mot_de_passe():
    """
    
    
    """

    mot_de_passe_attendu = os.environ['mot_de_passe_attendu']

    try:
        tentatives_max = int(sys.argv[1])
    except:
        tentatives_max = 3

    print("Nombre de tentatives max : ", tentatives_max)

    input_user = ""
    while input_user != mot_de_passe_attendu and tentatives_max >0:
        input_user = input('Tape your password ')
        date_now = time.strftime("%Y-%m-%d", time.localtime())
        len_input = str(len(input_user))
        
        if input_user == mot_de_passe_attendu:
            print("Mot de passe correct. Accès autorisé.")
            with open("log-connexion.txt", 'a') as f:
                f.write(f"Connexion OK - {date_now}  len : {len_input}\n")
            break
        elif tentatives_max>1:
            with open("log-connexion.txt", 'a') as f:
                f.write(f"Connexion error - {date_now}  len : {len_input}\n")

            tentatives_max -=1
            print(f"Mot de passe incorrect. Il vous reste {tentatives_max} tentative(s).")

        else:
            print("Nombre maximal de tentatives atteint. Accès refusé.")
            with open("log-connexion.txt", 'a') as f:
                f.write(f"Connexion error - {date_now}  len : {len_input}\n")
            break


if __name__ == '__main__':
    print('Début de la recherche : ', sys.argv[1])
    get_article(sys.argv[1])

    print('Fin de la recherche !')