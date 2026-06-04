#Introduccion.
print("Este Programa Recorre Los Archivos De Un Directorio Indicado Desde La Linea De Comandos Y Muestra El Nombre, Tamaño Y Fecha De Modificacion De Aquellos Archivos Cuyo Tamaño Sea Mayor Al Valor Especificado Por El Usuario.")
import sys
import os
import time
#Extrae La Ruta De Acceso y El Peso Minimo.
Info=sys.argv[1:]
#Convierte El Peso De String a Un Valor Flotante.
PesoMinimo=float(Info[1])
#Obtiene La Lista De Archivos Que Se Encuentran En La Ruta Solicitada.
Archivos=os.listdir(Info[0])
for Archivo in Archivos:
    #Crea La Ruta Absoluta De Cada Archivo, Juntando La Ruta De La Carpeta y El Nombre Del Archivo.
    Ruta=os.path.join(Info[0], Archivo)
    #Obtiene El Tamaño De La Ruta Absoluta De Un Archivo.
    Tamaño=os.path.getsize(Ruta)
    #Valora Si El Tamaño Es Mayor O Igual A El Minimo Requerido, Si La Condición Se Cumple, Se Imprime El Nombre Del Archivo, Su Tamaño En MegaBytes y Su Ultima Fecha De Modificación.
    if Tamaño>=PesoMinimo:
        #Otiene La Fecha Del La Ultima Modificacion Con El Formato Del Sistema.
        Fecha=os.path.getmtime(Ruta)
        #Transforma La Fecha Con Formato Del Sistema a Un Formato Legible Por El Usuario.
        FechaFormateada=time.ctime(Fecha)
        #Imprime Los Resultados.
        print("Archivo: ", Archivo)
        #Convierte Bytes a MegaBytes, Con Formato De Dos Numeros Despues Del Punto.
        print(f"Tamaño: {Tamaño/(1024**2):.2f} MB")
        print("Fecha De Modificación: ", FechaFormateada, "\n")