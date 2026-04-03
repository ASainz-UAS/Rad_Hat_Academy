Num_S=input("Ingrese Un Numero De La Suerte: ")
if Num_S.isdigit():
    Caracteres=len(Num_S)
    print(f"El Numero Ingresado: {Num_S}, Es Un Entero y Contiene {Caracteres} Caracteres.")
else:
    print(f"El Numero Ingresado: {Num_S}, No Es Un Entero.")