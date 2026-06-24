#Introduccion.
print("Este algoritmo obtiene una lista de tareas desde una API en formato JSON, separa las tareas completadas y no completadas, las guarda en archivos locales y finalmente calcula cuántas tareas han sido completadas en total.")
import requests
import json
#Extrae La Informacion De Una Pagina Web.
Información=requests.get("https://jsonplaceholder.typicode.com/todos")
#Convierte La Información A JSON.
Tareas=Información.json()
#Crea Unos Diccionarios Para Almacenar Las Tareas Completas y Incompletas.
TareasCompletas=[]
TareasIncompletas=[]
Contador=0
#Verifica Si La Tarea Esta Completa.
for Tarea in Tareas:
    if Tarea["completed"]==True:
        Contador+=1
        TareasCompletas.append(Tarea)
    else:
        TareasIncompletas.append(Tarea)
#Crea Un Archivo JSON Con Las Tareas Incompletas.
with open("Capitulo 11 JSON/Ejercicio 3/TareasIncompletas.json", "w", encoding="utf-8") as f:
    json.dump(TareasIncompletas, f)
#Imprime Un Mensaje Comparativo De Cuantas Tareas Hay Hechas Contra El Total De Tareas.
print(f"Se realizan {Contador} de {len(Tareas)} tareas")