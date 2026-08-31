class Fila:
    def __init__(self):
    self.fila = []

    def entrar(self, documneto):
        self.fila.append(documento)
    
    def imprimir(self):
        if len(self.fila) > 0:
            documento = self.fila.pop()
            print("imprimido",documento)
        else:
            return "nada"
    
    def mostrar(self):
        print(self.fila)

spooler = Fila()

spooler.entrar("1")
spooler.entrar("2")
spooler.entrar("3")
spooler.entrar("4")

spooler.mostrar()

spooler.imprimir()
spooler.imprimir()

spooler.mostrar()



