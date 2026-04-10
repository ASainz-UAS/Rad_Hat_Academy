#Introducción.
print("Este Programa Imprime Los Numeros Del 0 Al 49 Organizados En Filas De 10 Valores.")
#Imprime Todos Los Numeros Del 0 Al 49 En Forma De Tabla.
for i in range (0,50):
    print(i, end=" ")
    #Suma 1 A Cada 'i', y Cumple La Función Cuando 'i/10=0 (Como Residuo), y Los Separa Cada 10 Numeros.
    if (i+1)%10==0:
        print()