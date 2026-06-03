#Introduccion:
print("Este Programa Imprime El Numero De Lineas, Palabras y Caracteres De Un Archivo Que Se Lee Atraves De La Terminal.")
import sys
#Captura El Archivo Que Se Envia En La Terminal.
archivo=sys.argv[1]
#Abre El Archivo y Lo Lee.
contenido=open(archivo,'r').read()
#Cuenta Las Lineas, Palabras y Caracteres De Un Archivo.
lineas=len(contenido.splitlines())
palabras=len(contenido.split())
caracteres=len(contenido)
#Imprime Los Resultados.
print("Contenido:\n", contenido)
print("\nLineas:", lineas)
print("Palabras:", palabras)
print("Caracteres:", caracteres)