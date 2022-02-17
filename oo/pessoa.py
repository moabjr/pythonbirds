class Pessoa:
    def __init__(self, *filhos, nome=None, idade=41):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    moab = Pessoa(renzo,nome='Moab')
    print(Pessoa.cumprimentar(moab))
    print(id(moab))
    print(moab.cumprimentar())
    print(moab.nome, moab.idade)
    for filho in moab.filhos:
        print('O nome do filho do ' + moab.nome +' é ' + filho.nome)
