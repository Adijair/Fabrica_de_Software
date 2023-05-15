maior_peso = float('-inf')  # menor valor possível para o maior peso
menor_peso = float('inf')   # maior valor possível para o menor peso

for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i}: "))

    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

print(f"Maior peso lido: {maior_peso} kg")
print(f"Menor peso lido: {menor_peso} kg")
