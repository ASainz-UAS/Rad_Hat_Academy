def imprimir (Conteo):
    i=1
    print("\nLista Final: ")
    for Nombre, Cantidad in Conteo.items():
        print(f"{i}º {Nombre}")
        print(f"Cantidad: {Cantidad}.")
        i=i+1