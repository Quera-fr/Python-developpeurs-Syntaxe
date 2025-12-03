from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import pandas as pd
import os

from dawan.database import DataBase

app = FastAPI(
    title='My API',
    description='Première API DAWAN',
)

# Root principale
@app.get("/", tags=["Info"])
def hello():
    return "Hello World"

# Root avec envoi de parametres
@app.get('/square', tags=['Numeric'])
def square(n:int=0):
    return n**2


# Root avec envoi de fichiers
@app.post("/upload_file", tags=["Info"])
def upload_file(file:UploadFile=File(...)):
    return file.filename

# Structure de données
class UserInfo(BaseModel):
    age:int=0
    name:str='None'
    city:str='Lyon'


# Root avec structure de données
@app.post("/user_info", tags=["User"])
def get_user_inf(data:UserInfo):
    data = data.model_dump()
    print(data)
    return data


from dawan.database import DataBase




# Root de traitement de données
@app.post('/add_user', tags=['User'])
def add_user(data:UserInfo):

    # Connexion à la Base de données
    database = DataBase('user_info')

    # Création de la table
    database.create_table('users', name='TEXT', age='INTEGER', city='INTEGER')

    # Insertion dans la base de données
    database.insert_to_table('users', 
                             name=data.name, 
                             age=data.age,
                             city=data.city)
    
    print('Data added')
    return data.model_dump()
