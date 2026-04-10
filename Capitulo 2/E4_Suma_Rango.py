#Introducción.
print("Este Programa Solicita Numeros Enteros y Elabora La Suma Entre Todos Los Numeros Dentro De Ellos.")
#Solicita Al Usuario Ingresar Los Valores.
Num1=int(input("Introduzca El Primer Numero: "))
Num2=int(input("Introduzca El Segundo Numero: "))
#Declara Una Nueva Variable.
suma=0
#Suma Todos Los Numeros Entre 'Num1' y 'Num2'.
for i in range (Num1,Num2+1):
    suma=suma+i
#Imprime El Resultado.
print(f"El Total De La Suma Es: {suma}.")