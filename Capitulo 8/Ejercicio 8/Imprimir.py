def imprimir (NombresRepetidos, Nombres1, Nombres2, Archivos):
    i=1
    print("\nContenido De:", Archivos[0])
    for Nombre in Nombres1:
        print(f"{i}º {Nombre}")
        i=i+1
    i=1
    print("\nContenido De:", Archivos[1])
    for Nombre in Nombres2:
        print(f"{i}º {Nombre}")
        i=i+1
    i=1
    print("\nRepetidos: ")
    for Nombre in NombresRepetidos:
        print(f"{i}º {Nombre}")
        i=i+1