def total (archivo):
    archivo.remove("-t")
    Tc=int(0)
    Tp=int(0)
    Tl=int(0)
    #Abre Cada Archivo.
    for i in archivo:
        #Abre El Archivo y Lo Lee.
        contenido=open(i,'r').read()
        #Cuenta Las Lineas, Palabras y Caracteres De Un Archivo.
        lineas=len(contenido.splitlines())
        #Elabora Un Contador Que Da La Cantidad De Lineas De Todos Los Archivos.
        Tl=Tl+lineas
        palabras=len(contenido.split())
        #Elabora Un Contador Que Da La Cantidad De Palabras De Todos Los Archivos.
        Tp=Tp+palabras
        caracteres=len(contenido)
        #Elabora Un Contador Que Da La Cantidad De Caracteres De Todos Los Archivos.
        Tc=Tc+caracteres
        #Imprime El Contenido De Cada Archivo.
        print(f"\nContenido '{i}':\n")
        print(contenido)
    #Imprime El Total De LIneas, Palabras y Caracteres De Un Archivo.
    print("\nTotales De Los Archivos: ")
    print("Lineas:", Tl)
    print("Palabras:", Tp)
    print("Caracteres:", Tc)