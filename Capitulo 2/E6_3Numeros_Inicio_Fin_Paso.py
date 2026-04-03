print("Este Programa Pide Tres Numeros (Inicio, Fin Y Paso) Y Muestra Los Valores En Ese Rango Segun El Incremento Indicado.")
Inicio=int(input("Ingrese El Inicio Del Algoritmo: "))
Fin=int(input("Ingrese El Fin Del Algoritmo: "))
Paso=int(input("Ingrese Con Que Paso Ira El Algoritmo: "))
for i in range (Inicio,Fin,Paso):
    print(i)