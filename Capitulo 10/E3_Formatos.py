#Introduccion.
print("Este Programa Verifica Si Una Línea Está Correctamente Formateada Con Un Identificador De Dos Dígitos Y Dos Letras Mayúsculas, Seguido De Una Descripción, E Imprime Cada Parte Por Separado.")
import re
Info=input("Introduzca La Información: ")
#Separa La Información En Grupos y Con Un Formato Especifico.
Info_Formateada=re.search("(^\d{2})([A-Z]{2}\s)+(.*)$", Info)
if Info_Formateada:
    Identificador_1=Info_Formateada.group(1)
    Identificador_2=Info_Formateada.group(2)
    Descripcion=Info_Formateada.group(3)
    #Imprime Los Resultados
    print("Identificador (Numeros):", Identificador_1)
    print("Identificador (Letras):", Identificador_2)
    print("Descripción:", Descripcion)
else:
    print("Esta Información No Esta Formateada Correctamente...")