#Introducción.
print("Este Programa Define Una Funcion Que Recibe Dos Listas Como Parametros Y Devuelve Una Nueva Lista Con Los Elementos Que Son Comunes En Ambas Listas.")
#Pide Al Usuario Una Lista En Una Sola Linea.
#Separa Cada Numero, y Los Almacena En Una Nueva Variable.
Lis1=input("Escriba Los Numeros Que Desea Ingresar A La Primera Lista: ")
Lista1=Lis1.split()
Lis2=input("Escriba Los Numeros Que Desea Ingresar A La Segunda Lista: ")
Lista2=Lis2.split()
#Función Principal:
def comunes(l1,l2):
    Comun=[]
    #Valora Si Cada Elemento De La Primera Lista Esta En La Segunda.
    for i in l1:
        if i in l2:
            Comun.append(i)
    return Comun
Res_Comun=comunes(Lista1,Lista2)
#Imprime El Resultado Del Algoritmo.
print(f"Los Comunes En Las 2 Listas Son: {Res_Comun}.")



