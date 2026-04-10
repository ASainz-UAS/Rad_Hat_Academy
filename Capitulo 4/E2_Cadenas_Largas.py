#Introducción.
print("Este Programa Calcula La Longitud De La Cadena Más Larga En Una Colección Y Utiliza Ese Valor Para Mostrar Todas Las Cadenas Alineadas Correctamente.")
#Solicita Al Usuario Ingresar Los Valores.
print("Introduzca La Palabra 'end' Para Salir")
def cadenas():
    Cadenas=[]
    prompt = "Introduzca Una Palabra: "
    while True:
        Palabra=input(prompt)
        #Valora Si El Usuario Termino De Ingresar Los Valores.
        if Palabra=="end":
            break
        else:
            #Ingresa Los Valores A Una Lista De Strins.
            Cadenas.append(Palabra)
    return Cadenas
#Inicializa Las Variables Locales A Globales:
Cadenas=cadenas()
#Fución Principal:
def longitud(Cadenas):
    #Declara Una Variable.
    Mayor=0
    for i in Cadenas:
        #Valora Que 'i' Tiene Mas Caracteres.
        if len(i)>Mayor:
            Mayor=len(i)
    return Mayor
#Extrae Los Palabras Ordenadas Por Longitud.
Max=longitud(Cadenas)
#Imprime Cada Palabra Con Formato.
for i in Cadenas:
    print(i.ljust(Max))