# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import math

DESTRUIDO = 'Destruido'
ATIVO = 'Ativo'
GRAVIDADE = 10  # m/s^2


class Ator():
    """
    Classe que representa um ator. Ele representa um ponto cartesiano na tela.
    """
    _caracter_ativo = 'A'
    _caracter_destruido = ' '

    def __init__(self, x=0, y=0):
        """
        Método de inicialização da classe. Deve inicializar os parâmetros x, y, caracter e status

        :param x: Posição horizontal inicial do ator
        :param y: Posição vertical inicial do ator
        """
        self.y = y
        self.x = x
        self.status = ATIVO

    def caracter(self):
        return self._caracter_ativo if self.status == ATIVO else self._caracter_destruido

    def calcular_posicao(self, tempo):
        return self.x, self.y

    def colidir(self, outro_ator, intervalo=1):
        if self.status == ATIVO and outro_ator.status == ATIVO:
            delta_x = abs(self.x - outro_ator.x)
            delta_y = abs(self.y - outro_ator.y)
            if delta_x <= intervalo and delta_y <=intervalo:
                self.status=outro_ator.status=DESTRUIDO



class Obstaculo(Ator):
    _caracter_ativo = 'O'


class Porco(Ator):
    _caracter_ativo = '@'
    _caracter_destruido = '+'


class DuploLancamentoExcecao(Exception):
    pass


class Passaro(Ator):
    velocidade_escalar = '10'


    def __init__(self, x=0, y=0):
        super().__init__(x, y)
        self._x_inicial = x
        self._y_inicial = y
        self._tempo_de_lancamento = None
        self._angulo_de_lancamento = None  # radianos

    def foi_lancado(self):
        return not self._tempo_de_lancamento is None

    def colidir_com_chao(self):
        if self.y<= 0:
            self.status = DESTRUIDO

    def calcular_posicao(self, tempo):
        if self._esta_voado():
            delta_t = tempo-self._tempo_de_lancamento
            self._calcular_posicao_vertica(delta_t)
            self._calcular_posicao_vertica(delta_t)
        return super().calcular_posicao(tempo)


    def _calcular_posicao_vertica(self, delta_t):
        y_atual = self._y_inicial
        angulo_radianos= self._angulo_de_lancamento
        y_atual += self.velocidade_escalar*delta_t* math.sin(angulo_radianos)
        y_atual -= (GRAVIDADE * (delta_t ** 2)) / 2
        self.y = y_atual
    def _calcular_posicao_horizontal(self, delta_t):
        x_atual =  self._x_inicial
        angulo_radianos= self._angulo_de_lancamento
        x_atual = self.velocidade_escalar*delta_t* math.cos(angulo_radianos)
        self.x = x_atual
    def lancar(self, angulo, tempo_de_lancamento):
        self._angulo_de_lancamento = angulo
        self._tempo_de_lancamento = tempo_de_lancamento

    def _esta_voado(self):
        return self.foi_lancado() and self.status == ATIVO


class PassaroAmarelo(Passaro):
    _caracter_ativo = 'A'
    velocidade_escalar = 30
    _caracter_destruido = 'a'

class PassaroVermelho(Passaro):
    _caracter_ativo = 'V'
    _caracter_destruido = 'v'
    velocidade_escalar = 20