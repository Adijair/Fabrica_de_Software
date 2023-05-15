numeros = []    

continuar = True

while continuar:
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

    opcao = input("Deseja continuar digitando valores? (S/N) ")

    if opcao.upper() == 'N':
        continuar = False

media = sum(numeros) / len(numeros)
maior = max(numeros)
menor = min(numeros)

print("Média:", media)
print("Maior número:", maior)
print("Menor número:", menor)
