from flask import Flask
import requests
import random
import json

################################################
#   AQUI HACEMOS EL REQUEST HTTP A LA API DE hellcase
#####################################################
cookie = dict(hellcase_session="")  #aqui poner la cookie de 'hellcase_session'

def diario():
    url = "https://api.hellcase.com/csgo/dailyfree/buy?game=csgo"

    r = requests.get(url, cookies=cookie)
    
    tiempo = json.loads(r.content)

    return tiempo['time_left']

def balance():
    url = "https://api.hellcase.com/csgo/en/profile/get_profile_general_information/numero" #poner numero de perfil  en vez de 'numero'

    

    r = requests.get(url, cookies=cookie)
    
    saldo = json.loads(r.content)
    info = saldo['info']
    profile = info['profile']

    return profile['wallet_balance']


####################################
# SERVIDOR WEB PARA QUE SIEMPRE ESTE ACTIVO
#####################################

app = Flask(__name__)


@app.route('/')
def index():
  tiempo = str(diario())
  #dinero = str(balance())
  
  while True:
    # comprobar el 'time_left' de la respuesta
    if tiempo==0:
      tiempo=str(diario())
      #dinero = str(balance())
    return 


app.run(host='0.0.0.0', port=random.randint(1, 90000))

