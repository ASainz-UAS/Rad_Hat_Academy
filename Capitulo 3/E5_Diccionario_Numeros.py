#Introducción.
print("Este Programa Solicita Un Número Al Usuario Y Convierte Cada Dígito En Su Representación En Palabras En Español Utilizando Un Diccionario.")
#Declara y Inicializa Un Diccionario.
Numeros={"0":"Zero","1":"Uno","2":"Dos","3":"Tres","4":"Cuatro","5":"Cinco","6":"Seis","7":"Siete","8":"Ocho","9":"Nueve"}
#Solicita Al Usuario Ingresar Los Valores.
Num=input("Ingrese Un Numero: ")
#Imprime Los Resultados Solicitados.
for i in Num:
    print(f"{Numeros[i]}", end=" ")