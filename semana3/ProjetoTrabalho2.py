#usei biblioteca
import random

numeros = tuple(random.randint(1, 100) for _ in range(5))

print("Números gerados:", numeros)
print("Maior valor:", max(numeros))
print("Menor valor:", min(numeros))
