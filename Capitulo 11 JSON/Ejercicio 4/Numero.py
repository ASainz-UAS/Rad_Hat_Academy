#Introduccion.
print("Este algoritmo realiza una petición HTTP a una API de números, obtiene un dato curioso en formato JSON sobre un número ingresado y muestra el hecho devuelto por la API.")
import json
import requests
Numero=input("Ingrese Un Numero: ")
Enlace=f"http://numbersapi.com/{Numero}/math/?json&notfound=floor"
Informacion=requests.get(Enlace)
ArchivoJSON=Informacion.json()
print(ArchivoJSON["text"])