import requests

# TAREA 1: EXTRACCIÓN INICIAL DE CARRITOS

URL_CARTS = "https://dummyjson.com/carts?limit=0"

response = requests.get(URL_CARTS)

if response.status_code == 200:
    datos = response.json()
    carts = datos["carts"]

    print("Datos obtenidos correctamente")
    print("Total de carritos:", len(carts))
else:
    print("Error al obtener carritos:", response.status_code)
    exit()
