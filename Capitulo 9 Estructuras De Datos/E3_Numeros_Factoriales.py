#Introducción.
print("Este Programa Genera Un Diccionario Con Los Numeros Del 1 Al 9 Y Sus Respectivos Factoriales, Luego Multiplica El Factorial De 6 Por El Factorial De 5.")
from math import factorial
#Crea Un Diccionario Que Almecenan Los Vectoriales Dentro Del Rango De 1 a 10.
Factoriales={x:factorial(x) for x in range(1,10)}
#Multiplica 6! x 5!.
Resultado=Factoriales[6]*Factoriales[5]
#Imprime Los Resultados.
for Numero, Factorial in Factoriales.items():
    print("·", Numero,":", Factorial)
print("El Resultado De Multiplicar 6! x 5! Es:", Resultado)