print("Este Programa Solicita Texto Al Usuario Hasta Que Escriba 'end', Cuenta La Frecuencia De Cada Palabra Utilizando Un Diccionario Y Muestra Los Resultados Ordenados Por Palabra Y Por Frecuencia.")
print("Introduzca La Palabra 'end' Para Salir")
prompt = "Introduzca Una Palabra: "
Palabras={}
i=0
while True:
    Palabra=input(prompt)
    if Palabra=="end":
        break
    else:
        palabras=Palabra.split()
    for i in palabras:
        if i in Palabras:
            Palabras[i]+=1
        else:
            Palabras[i]=1
for palabra, cant in Palabras.items():
    print(palabra, ":", cant)