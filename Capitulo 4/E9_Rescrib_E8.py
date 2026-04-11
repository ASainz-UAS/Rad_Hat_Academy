#Introducción.
print("Este Programa Define Una Funcion Que Crea Otra Funcion Interna, Donde La Funcion Principal No Recibe Parametros Y La Funcion Anidada Recibe Dos Numeros Para Devolver Su Suma.")
#Pide Los Valores Para La Suma.
Num1=float(input("Ingrese Un Numero: "))
Num2=float(input("Ingrese Un Numero: "))
#Funciones Principales.
def funcion1 ():
    def funcion2 (v1,v2):
        return v1+v2
    return funcion2
#Captura La Función 1.
suma=funcion1()
resultado=suma(Num1,Num2)
#Imprime El resultado De la Suma.
#Ya No Se Pone () Por Que Ya No Aguarda Una Función, Si No Un Numero.
print(f"El total es: {resultado}")