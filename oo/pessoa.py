class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=41):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    moab = Pessoa(renzo,nome='Moab')
    print(Pessoa.cumprimentar(moab))
    print(id(moab))
    print(moab.cumprimentar())
    print(moab.nome, moab.idade)
    for filho in moab.filhos:
        print('O nome do filho do ' + moab.nome +' é ' + filho.nome)
    moab.sobrenome = 'Lima'
    del moab.filhos , moab.sobrenome

    print(moab.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos),id(moab.olhos),id(renzo.olhos))
    print(Pessoa.metodo_estatico(), moab.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), moab.nome_e_atributos_de_classe())