print("Este Programa Solicita Un Numero De La Suerte y Imprime Si Es Entero")
Num_S=input("Ingrese Un Numero De La Suerte: ")
if Num_S.isdigit():
    print(f"El Numero Ingresado: {Num_S}, Es Un Entero.")
else:
    print(f"El Numero Ingresado: {Num_S}, No Es Un Entero.")