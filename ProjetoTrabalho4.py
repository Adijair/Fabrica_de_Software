from datetime import date

ano_atual = date.today().year

menores = 0
maiores = 0

for i in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {i}: "))
    idade = ano_atual - ano_nascimento

    if idade < 18:
        menores += 1
    else:
        maiores += 1

print(f"Quantidade de pessoas menores de idade: {menores}")
print(f"Quantidade de pessoas maiores de idade: {maiores}")
