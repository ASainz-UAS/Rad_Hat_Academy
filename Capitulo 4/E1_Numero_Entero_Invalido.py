#Introducción.
print("Este Programa Define Una Función Que Solicita Un Número Entero Positivo, Valida La Entrada Y Devuelve El Número Si Es Correcto O Cero En Caso Contrario.")
#Fución Principal:
def numeros():
    #Solicita Al Usuario Ingresar Los Valores.
    num=int(input("Ingrese Un Numero: "))
    try:
        if num>0:
            return num
        else:
            return 0
    except:
        return 0
#Captura El Valor De La Fución En Una Nueva Variable.
resultado=numeros()
#Valora El Numero Es Positivo O Si No Lo Es Imprime 0.
if resultado==0:
    print(resultado)
else:
    print("Número válido: ", resultado)