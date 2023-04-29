#faça um progama em que diga se o número inteiro digitado na tela é par ou impar

numero = int(input('Me diga um numero: '))
resutado = numero % 2
if resutado == 0:
    print('O numero {} é par '. format(numero))
else:
    print('O numero {} é inpar '. format(numero))