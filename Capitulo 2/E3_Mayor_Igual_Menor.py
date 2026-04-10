#Introducción.
print("Este Programa Solicita 2 Numeros Enteros y Valora Si Son Iguales O Quien Es Mayor.")
#Solicita Al Usuario Ingresar Los Valores.
Num1=float(input("Introduzca El Primer Numero: "))
Num2=float(input("Introduzca El Segundo Numero: "))
#Valora Si Son Iguales, Menores O Iguales.
if Num1>Num2:
    print(f"El {Num1} Es Mayor Que {Num2}.")
elif Num1==Num2:
    print(f"Los Numeros {Num1} y {Num2} Son Iguales.") 
else:
    print(f"El {Num2} Es Mayor Que {Num1}.")