frase = "treinamento hoje de backend"
print("Frase atual:", frase)

palavra = input("Digite a palavra que deseja trocar: ")
palavra_nova = input("Digite a nova palavra: ")

palavra_nova = frase.replace(palavra, palavra_nova)

print("Nova frase:", palavra_nova)
