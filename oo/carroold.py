# coding=utf-8
""""
    voce deve criar uma classe carro que vai possuir dois atributos compostos
    por outras duas classes:

    1) Motor
    2) Direção

    O Motor terá a responsabilidade de controlar a velocidade.
    Ele oferece os seguintes atributos:
    1) Atributo de dado velocidade
    2) Método acelerar, que deverá incrementar a velocidade de um unidade
    3) Método frear, que devera decrementar a velocidade em duas unidades

    A Direçao terá a responsabilidade de controlar a direção. Ela oferece
    os seguintes atributos:
    1) valor de direção com os valores possíveis: Norte, Sul, Leste, Oeste
    2) Método girar a direita
    3) Método girar a esquerda

      N
    O    L
      S

    Exemplo:

    Exemplo:

    >>> # Testando motor

    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""
class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.velocidade += 1
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = range(0,self.velocidade)

class Direcao:

    ir_a_esquerda = list['Norte', 'Oeste', 'Sul', 'Leste']

    ir_a_direita = list['Norte', 'Leste', 'Sul', 'Oeste']

    def __init__(self):
        self.posicao = 'Norte'

    def girar_a_direita(self):
        self.posicao = self.ir_a_direita[self.posicao]
        return self.posicao

    def girar_a_esquerda(self):
        self.posicao = self.ir_a_esquerda[self.posicao]
        return self.posicao

class Carro:

    def __init__(self, motor=Motor(), direcao=Direcao()):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()

if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    velocidade = Motor(motor.acelerar())
    print(velocidade)

    #direcao = Direcao()
    #valor = direcao(valor='Norte')
    #print(direcao.valor)
    #posicao = 0

    #posicao += 1
    #print(girar_a_direita)
    #print(girar_a_esquerda)


