import random

opcoes = ["Pedra", "Papel", "Tesoura"]

jogada_usuario = input("Digite sua jogada (Pedra, Papel ou Tesoura): ")

if jogada_usuario not in opcoes:
    print("Jogada inválida. Digite uma das opções válidas.")
else:
    jogada_computador = random.choice(opcoes)

    print("Jogada do usuário:", jogada_usuario)
    print("Jogada do computador:", jogada_computador)

    if jogada_usuario == jogada_computador:
        print("Empate!")
    elif (
        (jogada_usuario == "Pedra" and jogada_computador == "Tesoura") or
        (jogada_usuario == "Papel" and jogada_computador == "Pedra") or
        (jogada_usuario == "Tesoura" and jogada_computador == "Papel")
    ):
        print("Você venceu!")
    else:
        print("Você perdeu!")
