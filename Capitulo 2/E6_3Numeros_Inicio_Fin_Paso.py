#Introducción.
print("Este Programa Pide Tres Numeros (Inicio, Fin Y Paso) Y Muestra Los Valores En Ese Rango Segun El Incremento Indicado.")
#Solicita Al Usuario Ingresar Los Valores.
Inicio=int(input("Ingrese El Inicio Del Algoritmo: "))
Fin=int(input("Ingrese El Fin Del Algoritmo: "))
Paso=int(input("Ingrese Con Que Paso Ira El Algoritmo: "))
#Muestra Los Valores En Ese Rango Segun El Incremento Indicado
for i in range (Inicio,Fin,Paso):
    print(f"{i},", end=" ")