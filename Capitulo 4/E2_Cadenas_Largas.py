print("Este Programa Calcula La Longitud De La Cadena Más Larga En Una Colección Y Utiliza Ese Valor Para Mostrar Todas Las Cadenas Alineadas Correctamente.")
print("Introduzca La Palabra 'end' Para Salir")
def cadenas():
    Cadenas=[]
    prompt = "Introduzca Una Palabra: "
    while True:
        Palabra=input(prompt)
        if Palabra=="end":
            break
        else:
            Cadenas.append(Palabra)
    return Cadenas
Cadenas=cadenas()
def longitud(Cadenas):
    Mayor=0
    for i in Cadenas:
        if len(i)>Mayor:
            Mayor=len(i)
    return Mayor
Max=longitud(Cadenas)
for i in Cadenas:
    print(i.ljust(Max))