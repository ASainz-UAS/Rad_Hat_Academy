print("Este Programa Solicita Varios Numeros En Una Sola Linea, Los Separa En Una Lista Y Muestra Solo Los Numeros Mayores Que Cero.")
Numeros_t=input("Escriba Los Numeros Que Desea Ingresar: ")
Numeros_L=Numeros_t.split()
for i in Numeros_L:
    print(i)
print("Mayores A 0: ")
for i in Numeros_L:
    if int(i)>0:
        print(i)







