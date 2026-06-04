#Introduccion.
print("Este programa copia un archivo de texto a otro. Puede obtener los nombres de los archivos desde la línea de comandos o solicitarlos al usuario si no se proporcionan los argumentos necesarios.")
import sys
#Extrae Los Nombres De Los Archivos Desde La Linea De Comandos.
Archivos=sys.argv[1:]
#Abre Los Archivos
Archivo=open(Archivos[0], "r")
ArchivoNuevo=open(Archivos[1], "w")
#Copia Cada Linea De Archivo De Entrada Al De Salida.
Lineas=Archivo.readline()
while Lineas!="":
    ArchivoNuevo.write(Lineas)
    Lineas=Archivo.readline()
print("Archivo Copiado...")