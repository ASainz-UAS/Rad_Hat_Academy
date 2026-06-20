import Area_Circulo
import Area_Cuadrado
#Introducción.
print("Algoritmo Que Prosesa El Area De Un Circulo")
print("Uso De Decimales y Unidades De Medidas En Centimetros")
print("Opciones De Area: \n 1. Cuadrado \n 2. Circulo \n 3.Salir")
#Pregunta Sobre Que Opcion Eligue El Usuario.
Opc=input("Introduzca Una Opción: ")
#Verifica Que La Opción Ingresada Este En La Carculadora.
if Opc in ["1","2","3"]:
    if Opc=="3":
        print("Saliendo...")
    elif Opc=="1":
        lado=float(input("Escriba Un Lado Del Cuadrado: "))
        A=Area_Cuadrado.Area (lado)
        print(f"El Area Del Cuadrado Es: {A} Cm^2")  
    elif Opc=="2":
        radio=float(input("Escriba El Radio Del Circulo: "))
        radio=radio**2
        B=Area_Circulo.Area (radio)
        print(f"El Area Del Circulo Es: {B} Cm^2")        
else:
    print("Opcion No Valida")