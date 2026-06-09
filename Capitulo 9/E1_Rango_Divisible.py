#Introducción.
print("Este Programa Genera Una Lista De Numeros Del 0 Al 99 Mediante Comprensiones De Listas Y Muestra Otra Lista Con Los Valores Divisibles Entre 5.")
#Crear La Lista Con Los Elementos Del 0 Al 99
Lista=[x for x in range(0,100)]
#Crear Una Lista Con Todos Los Elementos 
ListaN=[x for x in Lista if x%5==0]
#Imprimir Los Resultados.
print("Numeros Divisibles Entre 5: \n",*ListaN)