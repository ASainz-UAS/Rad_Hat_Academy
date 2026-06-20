#Introducción
print("Este Programa Define Una Funcion Que Recibe Varios Numeros En Una Sola Llamada Y Un Numero De Comparacion, Luego Cuenta Y Muestra Cuantos De Esos Numeros Son Mayores Que El Valor Indicado.")
#Solicita Al Usuario Ingresar Los Valores.
print("Introduzca La Palabra 'end' Para Salir")
#Declara Una Lista Vacia.
Nums=[]
while True:
    Numero=input("Introduzca Un Numero: ")
    #Valora Si El Usuario Termino De Ingresar Los Valores.
    if Numero=="end":
        break
    else:
        #Agrega El Valor Y Lo Convierte En Entero A Una Lista.
        Nums.append(int(Numero))
#Pide Un Numero De Comparación.
NumC=int(input("Ingrese El Numero De Comparación: "))
#Fución Principal:
def Mayor(Num,C):
    j=0
    Mayores_c=[]
    #Valora Si Cada 'i' Es Mayor Al Numero De Comparación.
    for i in Num:
        if i>C:
            Mayores_c.append(i)
    return Mayores_c
#Inicializa Las Variables Locales A Globales:
mayores_c=Mayor(Nums,NumC)
#Imprime Los Resultados Solicitados.
print(f"Los Numeros {Nums}\nSolo {len(mayores_c)} Son Mayores A {NumC} Los Cuales Son:\n{mayores_c}")