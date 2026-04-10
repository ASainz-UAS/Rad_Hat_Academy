#Introducción.
print("Este Programa Simula Una Calculadora Que Permite Realizar Operaciones Básicas Como Suma, Resta, Multiplicación Y División Utilizando Funciones.")
#Imprime El Menu De Opciones:
print("Opciones de la calculadora: \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Salir") 
#Funciones:
def suma(Num1,Num2):
    return Num1+Num2
def resta(Num1,Num2):
    return Num1-Num2
def multi(Num1,Num2):
    return Num1*Num2
def div(Num1,Num2):
    #Valora Si La Divición Se Puede Realizar.
    if Num2==0:
        return "Divicion Entre 0: ¡Error!"
    else:
        return Num1/Num2
#Pregunta Sobre Que Opcion Eligue El Usuario.
Opc=input("Introduzca Una Opción: ")
#Verifica Que La Opción Ingresada Este En La Carculadora.
if Opc in ["1","2","3","4","5"]:
    if Opc=="5":
        print("Saliendo...")
    else:
        #Pregunta y Captura Los Valores A Realizar Su Operación.
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
#Imprime Un Error Si La Opción Ingresada No Se Encuentra:
else:
    print("Opcion No Valida")