#Introducción.
print("Este Programa Solicita Valores Enteros Hasta Que El Usuario Lo Indique, Los Almacena En Un Lista Y Imprime La Suma Correspondiente.")
#Declara 2 Nuevas Variables.
Numeros=[]
Suma=0
#Solicita Al Usuario Ingresar Los Valores.
print("Introduzca La Palabra 'end' Para Salir")
while True:
    N=input("Introduzca Un Valor : ")
    if N=="end":
        break
    else:
        #Convierte 'N' De String A Entero.
        Numero=int(N)
        #Ingresa Cada 'Numero' A La Lista 'Numeros'.
        Numeros.append(Numero)
        #Suma La Suma Anterior Con El Ultimo Valor De La Lista 'Numeros'.
        Suma=Suma+Numeros[-1]
#Imprime Los Resultados Solicitados.
print(f"Los Valores {Numeros} \nDan En Total Una Suma De: {Suma}.")