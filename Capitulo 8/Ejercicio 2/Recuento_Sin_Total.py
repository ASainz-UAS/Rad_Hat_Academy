def default (archivo):
    #Abre Cada Archivo.
    for i in archivo:
        #Abre El Archivo y Lo Lee.
        contenido=open(i,'r').read()
        #Cuenta Las Lineas, Palabras y Caracteres De Un Archivo.
        lineas=len(contenido.splitlines())
        palabras=len(contenido.split())
        caracteres=len(contenido)
        #Imprime Los Resultados.
        print(f"\nContenido '{i}':\n")
        print(contenido)
        print("\nLineas:", lineas)
        print("Palabras:", palabras)
        print("Caracteres:", caracteres)