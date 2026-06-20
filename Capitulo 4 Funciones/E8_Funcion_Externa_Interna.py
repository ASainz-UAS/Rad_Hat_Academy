#Introducción.
print("Este Programa Define Una Funcion Que Crea Otra Funcion Interna, La Cual Utiliza Dos Numeros Recibidos Por La Funcion Principal Y Devuelve La Suma De Ambos Valores.")
#Pide Los Valores Para La Suma.
Num1=float(input("Ingrese Un Numero: "))
Num2=float(input("Ingrese Un Numero: "))
#Funciones Principales.
def funcion1 (v1,v2):
    def funcion2 ():
        return v1+v2
    return funcion2
#Captura La Función 1.
resultado=funcion1(Num1,Num2)
#Imprime El resultado De la Suma.
#Se Pone () Por Que No Guarda Un Numero, Si no, Una Funcion.
print(f"El total es: {resultado()}")