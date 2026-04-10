#Introducción.
print("Este Programa Pide Un Texto y Imprime El Total De Caracteres Ingresados.")
#Solicita Al Usuario Ingresar Los Datos.
Lin1=input("Ingrese Un Texto: ")
#Guarda El Numero De Caracteres (Sin Contar Espacios) En Una Nueva Variable.
TotalC=len(Lin1.replace(" ",""))
#Imprime Los Resultados Solicitados.
print(f"El Texto Ingresado Fue: {Lin1}.\nCon Un Total De {TotalC} Caracteres.")