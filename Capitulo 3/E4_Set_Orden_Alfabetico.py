#Introducción.
print("Este Programa Solicita Texto Al Usuario Hasta Que Escriba 'end', Almacena Las Palabras Unicas En Un Conjunto Y Muestra Las Palabras Ordenadas Junto Con Su Cantidad.")
#Declara 2 Variables.
Palabras=set()
i=0
#Solicita Al Usuario Ingresar Los Valores.
print("Introduzca La Palabra 'end' Para Salir")
while True:
    Palabra=input("Introduzca Una Palabra: ")
    if Palabra=="end":
        break
    else:
        #Si La Palabra Ingresada No Esta En El Conjunto 'Palabras', Procede A Añadirla.
        if Palabra not in Palabras:
            Palabras.add(Palabra)
#Ordena Las Palabras En Orden Alfabetico.
Palabras_Ordenadas=sorted(Palabras)
#Imprime Los Resultados Solicitados.
print(f"Las Palabras {Palabras_Ordenadas}\nSe Agregaron {len(Palabras)} Palabras.")