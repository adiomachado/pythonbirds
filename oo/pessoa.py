class Pessoa:
    def __init__(self, *filhos,  nome='None', idade=54):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    adio = Pessoa(nome='Adio') # faz o list de filhos
    luciano = Pessoa(adio, nome='Luciano') # os filhos da lista adio pertencem a Pessoa luciano
    print(Pessoa.cumprimentar(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filhos in luciano.filhos:
        print(filhos.nome)
    luciano.sobrenome = 'Ramalho' #cria atributo em tempo de execução
    del luciano.filhos      #remove atributos em tempo de execução
    print(luciano.__dict__) #mostra os atributos da Pessoa luciano
    print(adio.__dict__)    #mostra os atributos da Pessoa filho adio

