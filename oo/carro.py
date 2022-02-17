"""
Voce deve criar uma classe que vai possuir dois atributos compostos por duas classes
1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Metodo acelerar, que deverá incrementar a velocidade  de uma unidade
3) Metodo de frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferecerá os seguintes atributos:
1) Valor de direção com valores possiveis : Norte, Sul , Leste, Oeste
2) Metodo girar para a direita
3) Metodo girar para a esquerda
"""
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita_dict = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dict = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL

    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)