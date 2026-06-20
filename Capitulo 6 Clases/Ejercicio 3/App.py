#Introduccion.
print("Este programa extiende la clase Familia agregando métodos especiales que permiten comparar las instancias de Familia utilizando los operadores <, == y >, basados en la cantidad de hijos. De esta forma, las familias se pueden ordenar y comparar según su número de integrantes, ofreciendo una manera estructurada de evaluar las familias creadas." )
from Family import Familia
from Captura import cap_padre, cap_madre, cap_hijos
#Captura Los Datos De Las Familias, Atraves De Funciones Y Clases.
print("Familia 1")
p1=cap_padre()
m1=cap_madre()
hijos1=cap_hijos()
Fam1=Familia(p1, m1, *hijos1)
print("Familia 2")
p2=cap_padre()
m2=cap_madre()
hijos2=cap_hijos()
Fam2=Familia(p2, m2, *hijos2)
#Evalua Que Familia Tiene Más Hijos.
if Fam1>Fam2:
    print("La Familia 1 Tiene Mas Hijos")
elif Fam1==Fam2:
    print("Las 2 Familias Tienen Los Misma Cantidad De Hijos")
elif Fam1<Fam2:
    print("La Familia 2 Tiene Mas Hijos")