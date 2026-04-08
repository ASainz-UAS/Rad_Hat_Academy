print("Este Programa Simula Una Calculadora Que Permite Realizar Operaciones Básicas Como Suma, Resta, Multiplicación Y División Utilizando Funciones.")
print("Opciones de la calculadora:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
def suma(Num1,Num2):
    return Num1+Num2
def resta(Num1,Num2):
    return Num1-Num2
def multi(Num1,Num2):
    return Num1*Num2
def div(Num1,Num2):
    if Num2==0:
        return "Divicion Entre 0: ¡Error!"
    else:
        return Num1/Num2
Opc=input("Introduzca Una Opcion: ")
if Opc in ["1","2","3","4","5"]:
    if Opc=="5":
        print("Saliendo...")
    else:
        Num1=(float(input("Introduzca Un Numero: ")))
        Num2=(float(input("Introduzca Un Numero: ")))
        if Opc=="1":
            print("El Total De La Suma Es:",suma(Num1,Num2))  
        elif Opc=="2":
            print("El Total De La Resta Es:",resta(Num1,Num2))  
        elif Opc=="3":
            print("El Total De La Multiplicacion Es:",multi(Num1,Num2))  
        elif Opc=="4":
            print("El Total De La Divicion Es:",div(Num1,Num2))  
else:
    print("Opcion No Valida")