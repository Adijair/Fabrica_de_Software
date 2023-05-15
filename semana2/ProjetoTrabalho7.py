sexo = ""
while sexo != 'M' and sexo != 'F':
    sexo = input("Digite o sexo (M ou F): ")
    sexo = sexo.upper()

    if sexo != 'M' and sexo != 'F':
        print("Valor incorreto. Digite novamente.")

print("Sexo válido:", sexo)