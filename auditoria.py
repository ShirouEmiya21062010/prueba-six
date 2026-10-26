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
# TAREA 2: FILTRO DE DESCUENTOS

totales_por_carrito = []

for cart in carts:
    suma_validos = 0

    for product in cart["products"]:
        if product["discountPercentage"] < 12:
            suma_validos += product["quantity"]

    totales_por_carrito.append({
        "cartId": cart["id"],
        "userId": cart["userId"],
        "total": suma_validos
    })

print("Filtrado completado")
print("Carritos analizados:", len(totales_por_carrito))


# TAREA 3: IDENTIFICAR GANADOR Y CONSULTAR USUARIO

if not totales_por_carrito:
    print("No se encontraron carritos")
    exit()

ganador = totales_por_carrito[0]

for carrito in totales_por_carrito:
    if carrito["total"] > ganador["total"]:
        ganador = carrito

user_id = ganador["userId"]
max_productos = ganador["total"]

URL_USER = f"https://dummyjson.com/users/{user_id}"

response_user = requests.get(URL_USER)

if response_user.status_code == 200:
    usuario = response_user.json()

    print("Usuario ganador encontrado")
    print("ID:", user_id)
else:
    print("Error al obtener usuario:", response_user.status_code)
    exit()
