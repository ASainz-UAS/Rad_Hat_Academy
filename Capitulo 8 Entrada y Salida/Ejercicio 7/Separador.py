#Separa Cada Linea Del Archivo, Quitando Espacios y Saltos De Lineas.
def SepararArchivo (Archivo):
    #Separa Las Lineas De Los Archivos.
    Lineas=Archivo.readlines()
    Nombres=[]
    for Linea in Lineas:
        #Quita Espacios y Saltos De Linea.
        Nombres.append(Linea.strip())
    return Nombres