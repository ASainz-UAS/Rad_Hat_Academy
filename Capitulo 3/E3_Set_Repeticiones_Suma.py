#Introducción.
print("Este Programa Solicita Valores Enteros Hasta Que El Usuario Escriba 'end', Los Almacena En Un Conjunto Y Cuenta Cuantos Valores Repetidos No Se Agregan.")
#Inicializa Las Variables Ha Usar.
Numeros=set()
Suma=0
i=0
#Solicita Al Usuario Ingresar Los Valores.
print("Introduzca La Palabra 'end' Para Salir")
while True:
    N=input("Introduzca Un Valor: ")
    if N=="end":
        break
    else:
        #Convierte 'N' De String A Entero.
        Numero=int(N)
        #Valora Si El Valor Ingresado Ya Esta En El Conjunto.
        if Numero in Numeros:
            #En Casa De Esta Suma Un Contador, Que Registra Las Repeticiones.
            i=i+1
        else:
            #Si no, Lo Agrega Al Conjunto 'Numeros'.
            Numeros.add(Numero)
            #Elabora Una Suma De Cada Valor Del Conjunto.
            Suma=Suma+Numero
#Imprime Los Resultados Solicitados.
print(f"Los Valores {Numeros}\nSu Suma Es: {Suma}\nSe Intentaron Agregar {i} Numeros Repetidos.")