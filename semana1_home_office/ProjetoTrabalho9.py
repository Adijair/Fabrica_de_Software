frase = input("Digite uma frase: ")

numeros_letras = 0
for letra in frase:
    if letra.isalpha():
        numeros_letras += 1

print("A frase digitada tem", numeros_letras, "letras.")
