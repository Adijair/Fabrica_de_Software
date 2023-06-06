def ficha(nome="Desconhecido", gols=0):
    print(f"O jogador {nome} marcou {gols} gol(s).")

nome = input("Digite o nome do jogador: ")
gols = input("Digite a quantidade de gols marcados: ")

if nome.strip() == "":
    ficha(gols=int(gols))
else:
    ficha(nome, int(gols))