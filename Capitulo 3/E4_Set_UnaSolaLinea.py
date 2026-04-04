print("Este Programa Solicita Texto Al Usuario Hasta Que Escriba 'end', Almacena Las Palabras Unicas En Un Conjunto Y Muestra Las Palabras Ordenadas Junto Con Su Cantidad.")
prompt = "Introduzca Un Valor (O La Palabra 'end' Para Salir): "
Palabras=set()
i=0
while True:
    Palabra=input(prompt)
    if Palabra=="end":
        break
    else:
        if Palabra not in Palabras:
            Palabras.add(Palabra)
Palabras_Ordenadas=sorted(Palabras)
print(f"Las Palabras {Palabras_Ordenadas} y Se Agregaron {len(Palabras)} Palabras.")