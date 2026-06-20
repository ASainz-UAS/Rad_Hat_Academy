from Persona import Persona
#Captura Los Datos De Un Padre.
def cap_padre():
    print("Padre: ")
    Nom=input("Introduzca El Nombre: ")
    Padre=Persona(Nom)
    return Padre
#Captura Los Datos De Una Madre.
def cap_madre():
    print("Madre: ")
    Nom=input("Introduzca El Nombre: ")
    Madre=Persona(Nom)
    return Madre
#Captura Los Datos De Los Hijos.
def cap_hijos():
    hijos=[]
    i=1
    while True:
        print(f"Hijo #{i}")
        Nom=input("Introduzca El Nombre (Escriba 'end'): ")
        if Nom=="end":
            break
        hijos.append(Persona(Nom))
        i+=1
    return hijos