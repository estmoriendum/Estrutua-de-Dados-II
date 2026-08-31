class Pilha
    def __init__(self):
    self.pilha = []

    def empilhar(self, acao):
        self.pilha.append(acao)
    
    def desfazer(self):
        if len(self.pilha) > 0:
            return self.pilha.pop()
        else:
            return "nada"
    
    def mostrar(self):
        print(self.pilha)
    
    pilha = Pilha ()

    pilha.empilhar("1")
    pilha.empilhar("2")
    pilha.empilhar("3")

    pilha.mostrar()
    print("desfeito", pilha.desfazer())

    pilha.mostrar()
