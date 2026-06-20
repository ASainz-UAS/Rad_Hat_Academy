#Introducción.
print("Este Programa Genera Una Lista De Tuplas Con Los Numeros Del 5 Al 10 Y Sus Respectivos Factoriales.")
from math import factorial
#Crea Una Lista De Tuplas Que Almecenan Los Vectoriales Dentro Del Rango De 5 a 10.
Factoriales=[(x, factorial(x)) for x in range(5,11) ]
#Imprime Los Resultados.
for Factorial in Factoriales:
    print("·", Factorial)