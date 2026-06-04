#Introduccion.
print("Este programa copia un archivo de texto a otro y utiliza manejo de excepciones para detectar errores al abrir archivos, evitando que el programa falle inesperadamente.")
import sys
#Extrae Los Nombres De Los Archivos Desde La Linea De Comandos.
Archivos=sys.argv[1:]
#Verifica Si Existe El Arcchivo De Entrada, Si No, Cierra El Programa.
try:
    Archivo=open(Archivos[0], "r")
except OSError:
    print("El Archivo De Entrada No Existe.")
    sys.exit()
ArchivoNuevo=open(Archivos[1], "w")
#Copia Cada Linea De Archivo De Entrada Al De Salida.
Lineas=Archivo.readline()
while Lineas!="":
    ArchivoNuevo.write(Lineas)
    Lineas=Archivo.readline()
print("Archivo Copiado...")