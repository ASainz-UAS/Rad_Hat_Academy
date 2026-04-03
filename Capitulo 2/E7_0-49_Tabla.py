print("Este programa imprime los números del 0 al 49 organizados en filas de 10 valores.")
for i in range (0,50):
    print(i, end=" ")
    if (i+1)%10==0:
        print()