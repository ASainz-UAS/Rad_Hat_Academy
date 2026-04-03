print("Este programa concatena y limpia dos listas para formar correctamente los nombres de los días de la semana.")
Primero=["Domin", "Lu", "Mar", "Mier", "Jue", "Vier", "Saba"]
Segundo=["go", "nes", "tes", "coles", "ves", "nes", "do"]
Dias=[]
for i in range(len(Primero)):
    Dias.append(Primero[i]+Segundo[i])
print(Dias)