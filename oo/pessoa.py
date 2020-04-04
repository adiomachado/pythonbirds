class Pessoa:
    def __init__(self, *filhos,  nome='None', idade=54):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    adio = Pessoa(nome='Adio ,Davi ,João') # faz o list de filhos

    luciano = Pessoa(adio, nome='Luciano') # os filhos da lista adio pertencem a Pessoa luciano
    print(Pessoa.cumprimentar(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)
