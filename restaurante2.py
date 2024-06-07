#criando uma classe usando construtor
class Restaurante:
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
    def __str__(self):
       # return self.nome
        return f'{self.nome}|{self.categoria}|{self.ativo}'


print(restaurante_praca)