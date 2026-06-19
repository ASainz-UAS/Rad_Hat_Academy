#Introduccion.
print("Este Programa Permite Consultar Informacion De Libros Almacenados En Un Archivo JSON. El Usuario Ingresa El Titulo De Un Libro Y El Programa Busca Si Existe En Los Datos. Si Lo Encuentra, Muestra Su Informacion; De Lo Contrario, Indica Que El Libro No Se Encuentra Registrado.")
import json
#Abre y Cierra El JSON Automaticamente.
#Busca El JSON Con La Ruta De La Carpeta Que Lo Almacena y Lo Abre En Modo Lectura.
#Usa encoding="utf-8", Para Aceptar Caracteres Como ñ o Acentos.
with open("Capitulo 11/Ejercicio 1/books.json", "r", encoding="utf-8") as Libros:
    LibrosN=json.load(Libros)
print("Ingrese 'q' Para Salir.")
while True:
    Nombre=input("Ingrese Un Libro: ")
    #Utliza .lower() Que Cambia La Entrada A Minusculas.
    if Nombre.lower()=="q":
        print("Saliendo...")
        break
    else:
        #Busca El Libro He Imprime Su Información
        if Nombre.lower() in LibrosN:
            Libro=LibrosN[Nombre.lower()]
            for Tipoinfo, info in Libro.items():
                print(f"    ·{Tipoinfo}: {info}.")
        #Si No Lo Encuentra, Notifica Al Usuario.
        else:
            print("Libro No Encontrado...")