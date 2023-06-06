numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

numero = int(input("Digite um número entre 0 e 10: "))

if numero >= 0 and numero <= 10:
    extenso = numeros_extenso[numero]
    print(f"O número {numero} por extenso é: {extenso}")
else:
    print("Número inválido. Digite um número entre 0 e 10.")