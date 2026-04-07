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
    promedio=0
    for i in args:
        total+=i
    promedio=total/len(args)
    return total, promedio
total, promedio = suma(*Numeros)
print("El Total De La Suma Es:",total)
print("El Total Del Promedio Es: ",promedio)