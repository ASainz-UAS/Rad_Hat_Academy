#Introducción.
print("Este Programa Solicita Varios Numeros En Una Sola Linea, Los Separa En Una Lista Y Muestra Solo Los Numeros Mayores Que Cero.")
#Pide Al Usuario Un Numeros En Una Sola Linea.
Numeros_t=input("Escriba Los Numeros Que Desea Ingresar: ")
#Separa Cada Numero, y Los Almacena En Una Nueva Variable.
Numeros_L=Numeros_t.split()
#Muestra Todos Los Numeros Ingresados.
for i in Numeros_L:
    print(f"{i},", end=" ")
#Muestra Solo Los Mayores A Zero.
print("\nMayores A 0: ")
for i in Numeros_L:
    if int(i)>0:
        print(i)