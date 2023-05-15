casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de finaciamento? ')) #vou colocar em mes
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${} em {} anos'. format(casa, anos))
print(' a prestação será de R${}'. format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')