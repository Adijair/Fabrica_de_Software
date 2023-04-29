#faça um programa que pergunte a distância em km. calcular o preço da passagem, cobrando R$1.50 por km para viagens de até 200km e R$1.25 para viagens mais longas.

distancia_km = float(input("Qual a distancia da sua viagem: "))

if distancia_km <= 200:
    preco = distancia_km * 1.5
else:
    preco = distancia_km * 1.25

print("O preço da passagem é R${}".format(preco))