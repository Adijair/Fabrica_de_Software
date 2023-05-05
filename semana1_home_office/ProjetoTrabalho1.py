n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 == n2 == n3:
    print("Três iguais")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("Dois iguais")
else:
    print("Três diferentes")