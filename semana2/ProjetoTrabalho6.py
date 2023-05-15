soma_idade = 0
homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_de_20 = 0

for i in range(1, 5):
    print(f"---- Pessoa {i} ----")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M ou F): ")

    soma_idade += idade

    if sexo.upper() == "M" and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade

    if sexo.upper() == "F" and idade < 20:
        mulheres_menos_de_20 += 1

media_idade = soma_idade / 4

print(f"Média de idade do grupo: {media_idade:.2f} anos")
print(f"Nome do homem mais velho: {homem_mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_de_20}")
