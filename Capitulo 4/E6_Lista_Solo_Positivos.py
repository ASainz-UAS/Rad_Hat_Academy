#Introduccion:
print("Este Programa Pider Una Lista De Numeros y Muestra Solo Los Positivos (Usando Una Función)")
#Solicita Al Usuario Los Datos A Consultar:
Numeros=input("Escriba Los Numeros Que Desea Ingresar: ")
#Convierte Los Valores Ingresados De Tipo 'String' A 'Entero'.
Numeros_S = [int(i) for i in Numeros.split()]
#Funcion Principal:
def Positivo(Nums):
    #Inicializa Una Lista Vacia.
    Num_Pos=[]
    for i in Nums:
        if i>0:
            #Valora Si Los Valores Son Positivos, y Si Son Los Almacena En Una Lista.
            Num_Pos.append(i)
    return Num_Pos
#Imprime Solo Los Valores Positivos Ingresados
print(Positivo(Numeros_S))