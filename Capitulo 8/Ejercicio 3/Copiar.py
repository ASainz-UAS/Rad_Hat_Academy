#Introduccion.
print("Este programa copia el contenido de un archivo de texto a otro archivo, leyendo cada línea con readline() y escribiéndola en un nuevo archivo.")
#Pide El Nombre Del Archivo.
Entrada=input("Como Se Llama El Archivo De Entrada: ")
Salida=input("Como Se Llamara El Archivo De Entrada: ")
#Abre Los Archivos
Archivo=open(Entrada, "r")
ArchivoNuevo=open(Salida, "w")
#Copia Cada Linea De Archivo De Entrada Al De Salida.
Lineas=Archivo.readline()
while Lineas!="":
    ArchivoNuevo.write(Lineas)
    Lineas=Archivo.readline()
print("Archivo Copiado...")
Archivo.close()
ArchivoNuevo.close()