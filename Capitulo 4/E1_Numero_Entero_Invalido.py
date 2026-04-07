print("Este Programa Define Una Función Que Solicita Un Número Entero Positivo, Valida La Entrada Y Devuelve El Número Si Es Correcto O Cero En Caso Contrario.")
def numeros():
    num=input("Ingrese Un Numero: ")
    try:
        valor=int(num)
        if valor>0:
            return valor
        else:
            return 0
    except:
        return 0
resultado=numeros()
if resultado==0:
    print("Entrada no válida")
else:
    print("Número válido:", resultado)