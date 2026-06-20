#Introduccion.
print("Este Programa Crea Una Clase Familia Que Está Compuesta Por Dos Objetos Persona Que Representan A Los Padres Y Una Lista De Objetos Persona Que Representan A Los Hijos, Permite Almacenar Y Organizar La Información De Cada Integrante Y Solicita Datos Al Usuario Para Construir La Familia Completa.")
from Family import Familia
from Persona import Persona
#Captura Los Datos Del Padre y Madre.
print("Padre: ")
Nom=input("Introduzca El Nombre: ")
Eda=input("Introduzca La Edad: ")
print("M:Masculino, F:Femenino ")
Gen=input("Introduzca El Genero: ")
#Crea Una Nueva Persona Utilizando 'clases'.
Papa=Persona(Nom, Eda, Gen)
print("Madre: ")
Nom=input("Introduzca El Nombre: ")
Eda=input("Introduzca La Edad: ")
print("M:Masculino, F:Femenino ")
Gen=input("Introduzca El Genero: ")
Mama=Persona(Nom, Eda, Gen)
#Crea Una Lista Para Almacenar A Los Hijos.
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
#Envia y Captura Los Datos Creando Una Clase Familia.
Fam=Familia(Papa, Mama, *hijos)
#Imprime Los Resultados.
print("\nPadre: ")
print(Fam.Padre.getter_Nombre(), Fam.Padre.getter_Edad(), Fam.Padre.getter_Genero())
print("\nMadre: ")
print(Fam.Madre.getter_Nombre(), Fam.Madre.getter_Edad(), Fam.Madre.getter_Genero())
print("\nHijos: ")
for hijo in Fam.Hijos:
    print(hijo.getter_Nombre(), hijo.getter_Edad(), hijo.getter_Genero())