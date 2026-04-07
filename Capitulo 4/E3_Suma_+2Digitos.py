print("Este Programa Define Una Función Que Recibe Un Número Variable De Argumentos, Calcula La Suma De Todos Ellos Y Devuelve El Resultado.")
print("Introduzca La Palabra 'end' Para Salir")
Numeros=[]
while True:
    Numero=input("Introduzca Un Numero: ")
    if Numero=="end":
        break
    else:
        Numeros.append(int(Numero))
def suma(*args):
    total=0
    for i in args:
        total+=i
    return total
print("El Total Es:",suma(*Numeros))