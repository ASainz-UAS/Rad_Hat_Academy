def SumProm (s):
    suma=0; prom=0
    #Vuelve Float A Cada Elemento De 's'.
    s=[float(i) for i in s]
    for i in s:
        suma=suma+i
    prom=suma/len(s)
    print(f"La Suma Es: {suma}\nEl Promedio Es: {prom}")