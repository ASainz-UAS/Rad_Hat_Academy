print("Este Programa Solicita Valores Enteros Hasta Que El Usuario Lo Indique, Los Almacena En Un Lista Y Imprime La Suma Correspondiente.")
prompt = "Introduzca Un Valor (O La Palabra 'end' Para Salir): "
Numeros=[]
Suma=0
while True:
    data=input(prompt)
    if data=="end":
        break
    else:
        Numero=int(data)
        Numeros.append(Numero)
        Suma=Suma+Numeros[-1]
print(f"Los Valores {Numeros} Dan En Total Una Suma De: {Suma}.")