#Introducción.
print("Este Programa Define Una Funcion Que Recibe Un Numero Y Un Diccionario Como Parametros Y Agrega El Numero A Todos Los Valores Del Diccionario, Devolviendo El Diccionario Actualizado.")
#Diccionario Principal:
dic={"manzanas":10,"peras":5,"naranjas":8,"uvas":12,"mangos":6,"platanos":9}
#Pide Un Valor Para Aumentar.
Num=int(input("Ingrese El Numero De Aumento: "))
#Función Principal:
def aumento(valor,Diccionario):
    #Aumenta Cada Valor.
    for i in Diccionario:
        Diccionario[i]=Diccionario[i]+valor
    return Diccionario
#Llama A La Función.
Dic1=aumento(Num,dic)
#imprime El Resultado Del Algoritmo.
print(f"El Diccionario Con Su Aumento Queda Asi: {Dic1}.")