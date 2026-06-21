#Introducción:
print("Este algoritmo cuenta la frecuencia de palabras en un archivo de texto, limpiando caracteres y almacenando los resultados en un diccionario para luego guardarlos en un archivo JSON.")
import json
from Separador import Separar
#Se Usa Un Archivo.txt Para Mayor Eficiencia.
Archivo=open("Capitulo 11 JSON/Ejercicio 2/Ejemplo.txt", "r", encoding="utf-8").read()
#Separa Cada Palabra, Quitando Espacios, Saltos De Linea, Comillas y Tabulaciones.
ListaPalabras=Separar(Archivo)
Diccionario={}
#Corrabora Que La Palabra Se Encuentre y Suma Su Contador, Sino La Agrega.
for Palabra in ListaPalabras:
    if Palabra in Diccionario:
        Diccionario[Palabra]+=1
    else:
        Diccionario[Palabra]=1
#Almacena Un Diccionario En Un Archivo.JSON.
with open("Capitulo 11 JSON/Ejercicio 2/FrecuenciaPalabras.json","w", encoding="utf-8") as Archivojson:
    #El indent="\t" Sirve Para Agregar Una Tabulacion A Cada Elemento.
    json.dump(Diccionario,Archivojson, indent="\t")
#Imprime Las Palabras Con Su Frecuencia.
for Palabra, Frecuencia in Diccionario.items():
    print(f"La Palabra: {Palabra} Aparecio: {Frecuencia} Veses.")