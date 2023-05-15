import random

numero_pensado = random.randint(0, 10)
palpites = 0
acertou = False

while not acertou:
    palpite = int(input("Digite um número entre 0 e 10: "))
    palpites += 1

    if palpite == numero_pensado:
        acertou = True
        print("Parabéns! Você acertou o número.")
    elif palpite < numero_pensado:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

print("Total de palpites:", palpites)