class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

    if __name__ == '__main__':
        p = pessoa()
        print(pessoa.cumprimentar(p))
        print(id(p))
        print(p.cumprimentar())
