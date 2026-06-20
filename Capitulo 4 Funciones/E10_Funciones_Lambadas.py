#Introducción.
print("Este Programa Define Una Funcion Que Crea Una Funcion Anidada Utilizando Una Expresion Lambda Para Recibir Dos Numeros Y Devolver La Suma De Ambos.")
#Pide Los Valores Para La Suma.
Num1=float(input("Ingrese Un Numero: "))
Num2=float(input("Ingrese Un Numero: "))
#Funciones Principales.
def funcion1 (v1,v2):
    #Utiliza Una Función Lambada Como Una Función Anidada.
    suma=lambda:v1+v2
    return suma
#Captura La Función 1.
resultado=funcion1(Num1,Num2)
#Imprime El resultado De la Suma.
print(f"El total es: {resultado()}")