def maior(*valores):
    maior_valor = None
    for valor in valores:
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
    return maior_valor

resultado = maior(5, 9, 2, 7, 1)
print(f'O maior valor é: {resultado}')