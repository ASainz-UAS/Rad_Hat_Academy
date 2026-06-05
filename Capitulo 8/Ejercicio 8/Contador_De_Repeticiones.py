#Introducción.
print("Este Programa Lee Varios Archivos De Texto Indicados Desde La Linea De Comandos Y Cuenta Cuantas Veces Aparece Cada Nombre En Todos Los Archivos, Mostrando El Total De Apariciones De Cada Uno.")
from Separador import SepararArchivo
from Imprimir import imprimir
import sys
Archivos=sys.argv[1:]
Conteo={}
#Como No Se Sabe Cuantos Archivos Se Compararan Se Usa Un For.
for Archivo in Archivos:
    ArchivoN=open(Archivo, "r")
    Nombres=SepararArchivo(ArchivoN)
    #Valida Si Los Nombres Existen, y Si Existen, Incrementa Un Contador.
    for Nombre in Nombres:
        if Nombre in Conteo:
            Conteo[Nombre]=Conteo[Nombre]+1
        else:
            Conteo[Nombre]=1
#Imprime Los Resutados.
imprimir(Conteo)