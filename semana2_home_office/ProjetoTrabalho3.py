ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

idade = ano_atual - ano_nascimento

if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JUNIOR"
elif idade <= 20:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

print("Categoria:", categoria)