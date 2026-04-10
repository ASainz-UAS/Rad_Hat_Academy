#Introducción.
print("Este Programa Pide Tu Nombre y Apellidos Para Arrogarlos En Formato")
#Solicita Al Usuario Ingresar Los Valores.
Nom=input("Nombre: ")
Apellido1=input("Primer Apellido: ")
Apellido2=input("Segundo Apellido: ")
#Formatea Los Datos Ingresados En Este Formato: Juan, Perez, S.
Inicial_A2=Apellido2[0].upper()+"."
#Imprime Los Resultados Solicitados.
print(f"Nombre: {Nom}\nPrimer Apellido: {Apellido1}\nSegundo Apellido: {Apellido2}.")
print("Nombre Formateado:")
print(f"{Nom}, {Apellido1}, {Inicial_A2}")