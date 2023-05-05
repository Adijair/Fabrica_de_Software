# pede ao usuário uma string e uma palavra para verificar se está dentro da string
string = input("Digite uma string: ")
palavra = input("Digite uma palavra para verificar se está dentro da string: ")

# verifica se a palavra está dentro da string e exibe o resultado
if palavra in string:
    print("True")
else:
    print("False")
