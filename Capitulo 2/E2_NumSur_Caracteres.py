#Introducción.
print("este Algoritmo Pide Un Numero y Valora Si Este Es Entero Y Cuantos Caracteres Contiene.")
#Solicita Al Usuario Ingresar El Valor.
Num_S=input("Ingrese Un Numero De La Suerte: ")
#Valora Si Es Entero y Muestra La Cantidad De Caracteres Que Contiene.
if Num_S.isdigit():
    print(f"El Numero Ingresado: {Num_S}, Es Un Entero y Contiene {len(Num_S)} Caracteres.")
else:
    print(f"El Numero Ingresado: {Num_S}, No Es Un Entero.")