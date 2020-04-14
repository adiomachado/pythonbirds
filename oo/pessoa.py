
class Pessoa:
    olhos = 2    # atributo de classe ou default deve ser definido fora do def pois não alocam espaço na memoria
    def __init__(self, *filhos,  nome='None', idade=54):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    """
    faz o list de filhos
    """
    adio = Pessoa(nome='Adio')
    """
    Instancia Hoem no objeto luciano os filhos da lista adio pertencem a luciano
    """
    luciano = Homem(adio, nome='Luciano')
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

    print(Pessoa.olhos)
    print(luciano.olhos)
    print(adio.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(adio.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(adio, Pessoa))
    print(isinstance(adio, Homem))
    print(adio.olhos)
    print(luciano.cumprimentar())
    print(adio.cumprimentar())
