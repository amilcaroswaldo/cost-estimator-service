import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv
import json
# Cargar variables de entorno desde el archivo .env
# load_dotenv(dotenv_path="..env")
load_dotenv()
# Obtener valores de las variables de entorno
firebase_credentials_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
firebase_credentials_path =  json.loads(firebase_credentials_path)
databaseURL = os.getenv('DATABASEURL')
cred = credentials.Certificate(firebase_credentials_path)
# firebase_admin.initialize_app(cred)
firebase_admin.initialize_app(cred, {
    'databaseURL': databaseURL
})

ref = db.reference()