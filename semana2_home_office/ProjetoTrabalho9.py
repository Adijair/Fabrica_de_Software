while True:
    numero = int(input("Digite um número para ver a tabuada (ou um número negativo para sair): "))

    if numero < 0:
        break  

    print("Tabuada de", numero)
    for i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)

print("Programa encerrado.")
