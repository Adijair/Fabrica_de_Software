import random

vitorias_consecutivas = 0

while True:
    jogador = int(input("Digite um número (0 para par, 1 para ímpar): "))
    computador = random.randint(0, 1)
    soma = jogador + computador

    resultado = "par" if soma % 2 == 0 else "ímpar"

    print("Jogador:", jogador)
    print("Computador:", computador)
    print("Soma:", soma)
    print("Resultado:", resultado)

    if jogador != soma % 2:
        print("Você perdeu!")
        break

    vitorias_consecutivas += 1
    print("Você venceu!\n")

print("Total de vitórias consecutivas:", vitorias_consecutivas)