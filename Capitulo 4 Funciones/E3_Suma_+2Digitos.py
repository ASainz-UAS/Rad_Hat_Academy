#Introducción.
print("Este Programa Define Una Función Que Recibe Un Número Variable De Argumentos, Calcula La Suma De Todos Ellos Y Devuelve El Resultado.")
#Declara Una Lista Vacia.
Numeros=[]
#Solicita Al Usuario Ingresar Los Valores.
print("Introduzca La Palabra 'end' Para Salir")
while True:
    Numero=input("Introduzca Un Numero: ")
    #Valora Si El Usuario Termino De Ingresar Los Valores.
    if Numero=="end":
        break
    else:
        #Ingresa Los Valores A Una Lista De Enteros.
        Numeros.append(int(Numero))
#Fución Principal:
def suma(N):
    #Declara Una Nueva Variables.
    total=0
    #Suma Cada Valor Dado.
    for i in N:
        total+=i
    return total
#Imprime Los Resultados Solicitados.
print("El Total De La Suma Es:",suma(Numeros))