#Introduccion.
print("Este Programa Verifica Si La Entrada Es Un Número Entero Y Especifica Si Es Positivo O Negativo.")
import re
#Captura El Numero.
while True:
    #Valora Que Ingreses Un Numero Entero, y No Un Caracter Invalido.
    try:
        Numero=int(input("Ingrese Un Numero: "))
        break
    except ValueError:
        print("Solo Se Aceptn Numeros Enteros...")
#Busca El Signo '-', Para Validar Si Es Negativo.
Signo=re.search("^-", Numero)
#Si Numero Si Contine '-', La Variable Signo Aguarda Un 'Match' El En Este if Se Considera Con True.
if Signo:
    print("El Numero:", Numero, "Es Negativo.")
#Si Este No Contiene '-', Arroja Que El Numero Es Positivo.
else:
    print("El Numero:", Numero, "Es Positivo.")