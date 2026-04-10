#Introducción.
print("Este Programa Solicita Numeros Enteros y Elabora La Suma Entre Todos Los Numeros Dentro De Ellos.")
#Solicita Al Usuario Ingresar Los Valores.
Num1=int(input("Introduzca El Primer Numero: "))
Num2=int(input("Introduzca El Segundo Numero: "))
#Declara Una Nueva Variable.
suma=0
#Imprime La Suma De Todos Los Numeros Dentro Del Rango (Sin Importa Si El Numero De Inicio Es Mayor Al De Su Final).
if Num1>Num2:
    for i in range(Num2,Num1+1):
        suma=suma+i
else:
    for i in range(Num1,Num2+1):
        suma=suma+i
print(f"La Suma Final Es: {suma}.")