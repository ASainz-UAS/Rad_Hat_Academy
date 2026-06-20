#Introducción.
print("Este programa concatena y limpia dos listas para formar correctamente los nombres de los días de la semana.")
#Declara 2 Lista.
Primero=["Domin", "Lu", "Mar", "Mier", "Jue", "Vier", "Saba"]
Segundo=["go", "nes", "tes", "coles", "ves", "nes", "do"]
#Declara Una Lista Vacia.
Dias=[]
#Une Cada Valor De Las Dos Listas En Una Nueva Lista.
for i in range(len(Primero)):
    Dias.append(Primero[i]+Segundo[i])
#Imprime La Unión De Las 2 Listas.
print(Dias)