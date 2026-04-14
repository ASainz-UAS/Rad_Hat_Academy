import Area_Cir
#Introducción.
print("Algoritmo Que Prosesa El Area De Un Circulo")
print("Uso De Decimales y Unidades De Medidas En Centimetros")
#Solicita Al Usuario Ingresar El Radio.
radio=float(input("Escriba El Radio Del Circulo: "))
radio=radio**2
A=Area_Cir.Area (radio)
#Imprime Los Resultados Solicitados.
print(f"El Area Del Circulo Es: {A} Cm^2")