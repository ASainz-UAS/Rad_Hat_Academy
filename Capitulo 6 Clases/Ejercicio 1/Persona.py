#Introducción.
print("Este Programa Crea Una Clase Persona Que Almacena Nombre, Edad Y Género, Permite Mostrar Los Datos Guardados, Modificarlos Mediante Métodos Especiales Y Solicita Información Al Usuario Para Crear Y Actualizar Una Persona.")
#Clase Principal:
class Persona:
    def __init__(self, Nombre, Edad, Genero):
        self.Nombre=Nombre
        self.Edad=Edad
        self.Genero=Genero
    #gatter(Regresa Un Dato Guardado)
    def getter_Nombre(self):
        return self.Nombre
    def getter_Edad(self):
        return self.Edad
    def getter_Genero(self):
        return self.Genero
    #Regresa El Texto Con Formato.
    def __str__(self):
        return "Nombre: "+self.Nombre+", Edad: "+str(self.Edad)+", Genero: "+self.Genero+"."
    #Cambia O Actualiza Un Dato Ya Existente.
    def setter_Nombre(self, N_Nombre):
        self.Nombre=N_Nombre
    def setter_Edad(self, N_Edad):
        self.Edad=N_Edad
    def setter_Genero(self, N_Genero):
        self.Genero=N_Genero
#Pide Los Datos.
Nom=input("Introduzca El Nombre: ")
Eda=input("Introduzca La Edad: ")
print("M:Masculino, F:Femenino ")
Gen=input("Introduzca El Genero: ")
p1 = Persona(Nom, Eda, Gen)
print(p1)
#Pregunta Si Quieren Cambiar Un Dato y Imprimen El Resultado Con Los Datos Actualizados.
r=input("¿Quiere Cambiar Un Dato? y/n: ")
if r=="y":
    print("Introduzca Solo El Numero Correspondiente.")
    i=int(input("¿Que Dato Quiere Cambiar?\n1.Nombre\n2.Edad\n3.Genero\n4.Salir\n--> "))
    if i==4:
        print("Saliendo...")
        pass
    elif i==1:
        Nom=input("Introduzca El Nombre: ")
        p1.setter_Nombre(Nom)
        print(p1)
    elif i==2:
        Eda=int(input("Introduzca La Edad: "))
        p1.setter_Edad(Eda)
        print(p1)
    elif i==3:
        print("M:Masculino, F:Femenino ")
        Gen=input("Introduzca El Genero: ")
        p1.setter_Genero(Gen)
        print(p1)
else:
    print("Saliendo...")
    pass