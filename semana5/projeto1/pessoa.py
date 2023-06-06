class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar__info(self):
        return f'Olá me chamo {self.nome} e tenho {self.idade}'