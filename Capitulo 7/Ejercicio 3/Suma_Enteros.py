#Introducion.
print("Este Programa Pide Numeros Infinitos, Los Suma, Con Manejo De Exepciones.")
suma=0
while True:
    try:
        Num=int(input("Introduzca Un Numero: "))
        suma=suma+Num
    #Valora Si Se Puede Convertir En Entero.
    except ValueError:
        print("Numero Invalido.")
    #Valora Si Se Ingreso La Conbinacion Ctrl+C, Para Salir Del Programa.
    except KeyboardInterrupt:
        print("\nPrograma Finalizado...")
        break
    #Valora Si Se Ingreso La Conbinacion Ctrl+Z, Para Salir Del Programa e Imprime La Suma.
    except EOFError:
        print(f"La Suma Final Es: {suma}")
        break