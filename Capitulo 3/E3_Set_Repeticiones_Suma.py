print("Este Programa Solicita Valores Enteros Hasta Que El Usuario Escriba 'end', Los Almacena En Un Conjunto Y Cuenta Cuantos Valores Repetidos No Se Agregan.")
prompt = "Introduzca Un Valor (O La Palabra 'end' Para Salir): "
Numeros=set()
Suma=0
i=0
while True:
    data=input(prompt)
    if data=="end":
        break
    else:
        Numero=int(data)
        if Numero in Numeros:
            i=i+1
        else:
            Numeros.add(Numero)
            Suma=Suma+Numero
print(f"Los Valores {Numeros} Dan En Total Una Suma De: {Suma} y Se Intentaron Agregar {i} Numeros Repetidos.")