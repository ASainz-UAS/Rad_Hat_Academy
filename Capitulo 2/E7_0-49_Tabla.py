print("Este Programa Imprime Los Numeros Del 0 Al 49 Organizados En Filas De 10 Valores.")
for i in range (0,50):
    print(i, end=" ")
    if (i+1)%10==0:
        print()