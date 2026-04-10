#Introducción.
print("Este Programa Solicita Texto Al Usuario Hasta Que Escriba 'end', Cuenta La Frecuencia De Cada Palabra Utilizando Un Diccionario Y Muestra Los Resultados Ordenados Por Palabra Y Por Frecuencia.")
#Declara 2 Variables.
Palabras={}
i=0
#Solicita Al Usuario Ingresar Los Valores.
print("Introduzca La Palabra 'end' Para Salir")
while True:
    Palabra=input("Introduzca Una Palabra: ")
    if Palabra=="end":
        break
    else:
        #Agrega La Palabra Al Diccionario.
        palabras=Palabra.split()
    for i in palabras:
        if i in Palabras:
            #Suma 1 Al Contador De Repeticiones.
            Palabras[i]+=1
        else:
            Palabras[i]=1
#Muestra Las Palabras Ordenadas Por Frecuencia.
for palabra, cant in Palabras.items():
    print(palabra,":", cant)