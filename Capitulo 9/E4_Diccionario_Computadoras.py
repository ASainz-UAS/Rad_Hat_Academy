#Introducción:
print("Este Programa Genera Un Diccionario Anidado Que Agrupa Equipos De Computo Por Persona Y Acumula El Valor Total De Cada Tipo De Equipo.")
Computadoras={}
print("Ingrese 'end' Para Terminar El Programa.")
while True:
    Linea=input("Ingrese El Numbre, Producto y Precio: ")
    if Linea!="end":
        #Crea Una Lista Con Cada Dato Separado.
        Datos=Linea.split()
        #Separa Los Datos Por Su Tipo.
        Nombre=Datos[0]
        Tipo=Datos[1]
        Valor=int(Datos[2])
        #Si Nombre No Esta En Computadoras Lo Agrega y Crea Un Diccionario.
        if Nombre not in Computadoras:
            Computadoras[Nombre]={}
        #Si Tipo No Esta En El Nombre Lo Agrega y Le Asigna Su Valor.
        if Tipo not in Computadoras[Nombre]:
            Computadoras[Nombre][Tipo]=Valor
        #Si No Suma El Nuevo Valor Con El Aterior.
        else:
            Computadoras[Nombre][Tipo]+=Valor
    else:
        #Imprime Los Resultados.
        for Nombre, Equipos in Computadoras.items():
            print(Nombre, ":", Equipos)
        break



