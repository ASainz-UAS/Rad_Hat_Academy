#Introduccion:
print("Este Programa Pider Una Lista De Numeros y Muestra Solo Los Positivos")

#Pide Datos:
Numeros=input("Escriba Los Numeros Que Desea Ingresar: ")
Numeros_S = [int(i) for i in Numeros.split()]
#Funcion
def Positivo(Nums):
    Num_Pos=[]
    for i in Nums:
        if i>0:
            Num_Pos.append(i)
    return Num_Pos
print(Positivo(Numeros_S))
