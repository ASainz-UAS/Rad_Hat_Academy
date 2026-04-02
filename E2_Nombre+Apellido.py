print("Este Programa Pide Tu Nombre y Apellidos Para Arrogarlos En Formato")
Nom=input("Nombre: ")
Apellido1=input("Primer Apellido: ")
Apellido2=input("Segundo Apellido: ")
Inicial_A2=Apellido2[0].upper()+"."
print(f"Nombre: {Nom}, Primer Apellido: {Apellido1}, Segundo Apellido: {Apellido2}.")
print("Nombre Formateado:")
print(f"{Nom}, {Apellido1}, {Inicial_A2}")