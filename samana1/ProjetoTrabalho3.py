#faça um programa para sortear um aluno entre três
import random

aluno1 = str(input('Primeiro aluno:'))
aluno2 = str(input('segundo aluno:'))
aluno3 = str(input('Tecero aluno:'))

lista = [aluno1, aluno2, aluno3]

escolhido = random.choice(lista)
print('O aluno escolido foi {}'. format(escolhido))