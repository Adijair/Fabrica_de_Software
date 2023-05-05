nascimento = int(input("Digite o ano de nascimento: "))
ano = int(input("Digite o ano atual: "))
idade = ano - nascimento

if idade >= 18:
    print("Você é maior de idade e tem {} anos.". format(idade))
else:
    print("Você é menor de idade e tem {} anos.". format(idade))
