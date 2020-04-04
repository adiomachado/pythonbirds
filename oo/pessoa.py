class Pessoa:
    olhos = 2    # atributo de classe ou default deve ser definido fora do def pois não alocam espaço na memoria
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
    luciano.olhos = 1
    del luciano.olhos       #remove o atributo olhos do objeto luciano, permanecendo na classe
    print(luciano.__dict__) #mostra os atributos de instância da Pessoa luciano
    print(adio.__dict__)    #mostra os atributos de instância da Pessoa filho adio
    Pessoa.olhos = 4        #altera o atributo olhos da classe Pessoa
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(adio.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(adio.olhos))

