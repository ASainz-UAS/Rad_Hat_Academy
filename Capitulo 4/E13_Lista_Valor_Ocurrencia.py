#Introducción.
print("Este Programa Define Una Funcion Que Busca Un Elemento En Una Lista Y Devuelve El Indice Correspondiente A La Primera, Segunda O Tercera Ocurrencia Segun Se Indique.")
#Captura Una Lista:
Lis=input("Escriba Los Numeros Que Desea Ingresar A La Primera Lista: ")
Lista = [int(i) for i in Lis.split()]
Valor=int(input("¿Que Valor Desea Buscar? "))
lugar=int(input("¿En Que N-Veses Desea Buscar El Valor? "))
def buscar(l,v,x):
    contador=0
    for i in range(len(l)):
        if l[i]==v:
            contador+=1
            if contador==x:
                return i
    raise ValueError("No se encontró la ocurrencia")
resultado=buscar(Lista, Valor, lugar)
print(f"El Valor {Valor} Aparece En El Indice {resultado}.")

