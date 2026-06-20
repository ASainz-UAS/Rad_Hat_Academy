#Introducción.
print("Este Programa Arroga El Numero De Veses Que Aparece El Primer y Ultimo Caracter De Un Texto.")
#Solicita Al Usuario Ingresar El Texto.
Texto=input("Ingrese Un Texto Breve: ")
#Captura La Cantidad De Apariciones De La Inicial y El Ultimo Caracter.
Cant_Ini=Texto.count(Texto[0])
Cant_Fin=Texto.count(Texto[-1])
#Imprime Los Resultados Solicitados.
print(f"El Texto Ingresado Fue: {Texto}\nSu Primera Letra {Texto[0]} Se Repite Un Total De {Cant_Ini} Veses\nSu Ultima Letra {Texto[-1]} Se Repite Un Total De {Cant_Fin}")