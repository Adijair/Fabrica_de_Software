valores = []

for i in range(5):
    valor = float(input('Digite um valor: '))
    valores.append(valor)

maior = max(valores)
posicao_maior = valores.index(maior)

menor = min(valores)
posicao_menor = valores.index(menor)

print('Valores digitados:', valores)
print(f'O maior valor digitado foi {maior} na posição {posicao_maior}')
print(f'O menor valor digitado foi {menor} na posição {posicao_menor}')