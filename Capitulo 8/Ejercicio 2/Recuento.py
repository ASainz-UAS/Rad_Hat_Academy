#Introduccion:
print("Este Programa Cuenta y Muestra El Total De Lineas, Palabras y Caracteres De Todos Los Archivos Indicados En La Terminal Cuando Se Utiliza La Opcion -t.")
import sys
from Recuento_Sin_Total import default
from Recuento_Con_Total import total
#Captura Los Archivo Que Se Envia En La Terminal.
archivo=sys.argv[1:]
if archivo[0]=="-t":
    total(archivo)
else:
    default(archivo)