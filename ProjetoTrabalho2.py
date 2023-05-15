print('LOJINHA DO BUIÚ')
preço = float(input('preço das conpras: R$'))
print('''FORMAS DE PAGAMENTOS
[ 1 ] à vista dinhero/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão''')
opção = int(input('Qual é a opição?'))

if opção ==1:
    total = preço - (preço * 10 / 100)
elif opção ==2:
    total = preço - (preço * 5 / 100)
elif opção ==3:
    total = preço
    parcela = total / 2
    print('Sua compra')