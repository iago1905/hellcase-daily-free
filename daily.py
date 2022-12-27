import requests
import json

# Put cookies here
cookies = ["AAAAAAAAAAAAAAAAAAAAAAA",
          "BBBBBBBBBBBBBBBBBBBBBBBB",
          "CCCCCCCCCCCCCCCCCCCCCCCC",
          "DDDDDDDDDDDDDDDDDDDDDDDD"]

def realizar_solicitud(cookie_value):
    cookies = {'hellcase_session': cookie_value}
    try:
        r = requests.get("https://api.hellcase.com/dailyfree/buy", cookies=cookies)
        tiempo = json.loads(r.content)
        print(tiempo['time_left'])
    except Exception as e:
        print(f"Ocurrió un error al realizar la solicitud: {e}")

# Realizar solicitudes con diferentes cookies
for clave in cookies:
  realizar_solicitud(clave)
    
