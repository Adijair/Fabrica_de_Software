def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

s = soma(a, b)
print("Soma:", s)

sub = subtracao(a, b)
print("Subtração:", sub)

mult = multiplicacao(a, b)
print("Multiplicação:", mult)