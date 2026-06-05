#Separa Cada Linea Del Archivo, Quitando Espacios y Saltos De Lineas.
def SepararArchivo1 (Archivo1):
    #Separa Las Lineas De Los Archivos.
    Lineas1=Archivo1.readlines()
    Nombres1=[]
    for Linea in Lineas1:
        #Quita Espacios y Saltos De Linea.
        Nombres1.append(Linea.strip())
    return Nombres1
def SepararArchivo2(Archivo2):
    #Separa Las Lineas De Los Archivos.
    Lineas2=Archivo2.readlines()
    Nombres2=[]
    for Linea in Lineas2:
        #Quita Espacios y Saltos De Linea.
        Nombres2.append(Linea.strip())
    return Nombres2