1-tipo primitivos: 
-int(numeros interos)
-float
-
-str
-

2-tipo estruturas condicionais:
if, elif e else são palavras-chave em Python que permitem a execução condicional de blocos de código.

O if é utilizado para testar uma condição e executar um bloco de código se a condição for verdadeira. Por exemplo:

python
Copy code
num = 10
if num > 0:
    print("O número é positivo")
Nesse caso, o bloco de código dentro do if é executado porque a condição num > 0 é verdadeira.

O elif é uma abreviação de "else if" e é utilizado para testar uma condição adicional caso a condição anterior tenha sido falsa. Por exemplo:

python
Copy code
num = -10
if num > 0:
    print("O número é positivo")
elif num == 0:
    print("O número é zero")
else:
    print("O número é negativo")
Nesse caso, a primeira condição do if é falsa, então o programa testa a condição do elif e, como ela também é falsa, o programa executa o bloco de código do else.

O else é utilizado para executar um bloco de código caso todas as condições anteriores tenham sido falsas. Por exemplo:

python
Copy code
num = 0
if num > 0:
    print("O número é positivo")
elif num == 0:
    print("O número é zero")
else:
    print("O número é negativo")
Nesse caso, a primeira condição do if é falsa e a condição do elif é verdadeira, então o programa executa o bloco de código correspondente ao elif.

Em resumo, o if, elif e else permitem que o programa execute diferentes blocos de código de acordo com as condições que são testadas


referencias:
@CursoemVideo
codingame.com