#Introducción.
print("Este Programa Solicita Un Numero De La Suerte y Imprime Si Es Entero")
#Solicita Al Usuario Ingresar Un Valor.
Num_S=input("Ingrese Un Numero De La Suerte: ")
#Valora Si Es Positivo
if Num_S.isdigit():
    print(f"El Numero Ingresado: {Num_S}, Es Un Entero.")
else:
    print(f"El Numero Ingresado: {Num_S}, No Es Un Entero.")