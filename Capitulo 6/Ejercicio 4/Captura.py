#Introduccion.
print("Este programa crea diferentes tipos de trabajadores usando herencia, permitiendo calcular la pensión de cada uno según su salario y años trabajados.")
from Clases import Worker, Manager, Executive
print("Tipo De Trabajador:\n1.Trabajador.\n2.Manager.\n3.Ejecutivo.\n4.Salir.")
Tra=int(input("Escriba La Opción A Consultar: "))
if Tra==4:
    print("Saliendo...")
    pass
elif Tra==1:
    N=input("Nombre Del Trabajador: ")
    S=float(input("Salario Del Trabajador: "))
    A=float(input("Años De Antiguedad: "))
    Trabajador=Worker(N,S,A)
    print(f"El Trabajador: {Trabajador.name()}\nTiene Una Pension De: {Trabajador.Pension()}")
elif Tra==2:
    N=input("Nombre Del Gerente: ")
    S=float(input("Salario Del Gerente: "))
    A=float(input("Años De Antiguedad: "))
    Trabajador=Manager(N,S,A)
    print(f"El Gerente: {Trabajador.name()}\nTiene Una Pension De: {Trabajador.Pension()}")
elif Tra==3:
    N=input("Nombre Del Ejecutivo: ")
    S=float(input("Salario Del Ejecutivo: "))
    A=float(input("Años De Antiguedad: "))
    Trabajador=Executive(N,S,A)
    print(f"El Ejecutivo: {Trabajador.name()}\nTiene Una Pension De: {Trabajador.Pension()}")
else:
    print("Opcion No Valida.")
    print("Saliendo...")
    pass