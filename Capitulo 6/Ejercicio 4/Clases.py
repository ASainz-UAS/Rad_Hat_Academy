#Clases Con Herencias.
class Worker:
    def  __init__(self, Nom, Sal, Años):
        self.Nom=Nom
        self.Sal=Sal
        self.Años=Años
    #Crea Una Funcion Que Realiza El Calculo De Una Pension.
    def Pension(self):
        P=(self.Sal*0.10)*self.Años
        return P
    #Envia El Nombre Del Trabajador Atraves De Una Funcion.
    def name(self):
        return self.Nom
#Crea Clases HHeredando Las Fuciones Y Variables De Otra.
class Manager(Worker):
    def Pension(self):
        P=(self.Sal*0.20)*self.Años
        return P
class Executive (Manager):
    def Pension(self):
        P=(self.Sal*0.30)*self.Años
        return P