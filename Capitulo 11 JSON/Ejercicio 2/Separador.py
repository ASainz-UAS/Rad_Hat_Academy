def Separar(Texto):
    Texto=Texto.replace("\n", " ")
    Texto=Texto.replace("\t", " ")
    Texto=Texto.replace('"', ' ')
    ListaPalabras=Texto.split()
    return ListaPalabras