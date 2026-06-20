#Introduccion.
print("Este Programa Compara Los Nombres Almacenados En Dos Archivos De Texto Proporcionados Desde La Linea De Comandos E Imprime Solo Aquellos Nombres Que Aparecen En Ambos Archivos.")
import sys
from Imprimir import imprimir
from Separador import SepararArchivo
Archivos=sys.argv[1:]
Archivo1=open(Archivos[0],"r")
Archivo2=open(Archivos[1],"r")
Nombres1=SepararArchivo(Archivo1)
Nombres2=SepararArchivo(Archivo2)
#Busca Las Concidencias Entre Los Dos Archivos.
NombresRepetidos=[]
for Nombre in Nombres1:
    if Nombre in Nombres2:
        NombresRepetidos.append(Nombre)
imprimir(NombresRepetidos, Nombres1, Nombres2, Archivos)
Archivo1.close()
Archivo2.close()