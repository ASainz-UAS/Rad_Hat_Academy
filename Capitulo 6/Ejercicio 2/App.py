from Family import Familia
from Persona import Persona
print("Padre: ")
Nom=input("Introduzca El Nombre: ")
Eda=input("Introduzca La Edad: ")
print("M:Masculino, F:Femenino ")
Gen=input("Introduzca El Genero: ")
Papa=Persona(Nom, Eda, Gen)
print("Madre: ")
Nom=input("Introduzca El Nombre: ")
Eda=input("Introduzca La Edad: ")
print("M:Masculino, F:Femenino ")
Gen=input("Introduzca El Genero: ")
Mama=Persona(Nom, Eda, Gen)
hijos=[]
i=1
while True:
    print(f"Hijo #{i}")
    Nom=input("Introduzca El Nombre (Escriba 'end'): ")
    if Nom=="end":
        break
    Eda=input("Introduzca La Edad: ")
    print("M:Masculino, F:Femenino ")
    Gen=input("Introduzca El Genero: ")
    hijos.append(Persona(Nom, Eda, Gen))
    i+=1
Fam=Familia(Papa, Mama, *hijos)
print("\nPadre: ")
print(Fam.Padre.getter_Nombre(), Fam.Padre.getter_Edad(), Fam.Padre.getter_Genero())
print("\nMadre: ")
print(Fam.Madre.getter_Nombre(), Fam.Madre.getter_Edad(), Fam.Madre.getter_Genero())
print("\nHijos: ")
for hijo in Fam.Hijos:
    print(hijo.getter_Nombre(), hijo.getter_Edad(), hijo.getter_Genero())