#Introducción.
print("Este Algoritmo Pide Un Indice y Lo Busca En Una Lista De 10 Numeros Con Manejo De Exepciones. ")
Numeros=[1,250,45,23,9098,78,26,0,45,38]
print("Introduzca 'end' Para Terminar. ")
while True:
    Num=input("Introduzca Un Numero: ")
    if Num=="end":
        break
    try:
        i=int(Num)
        if i>=0:
            print(Numeros[i])
        else:
            raise IndexError
    #Valora Si Introdusco Una Letra O Decimal.
    except ValueError:
        print("No Se Pude Introducir Letras O Decimales. ")
    #Valora Si El Indice Introducido Esta Fuera De Rango.
    except IndexError:
        print("Indece Fuera De Rango.")