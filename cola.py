class Cola:
    def __init__(self):
        self.cola = []
        self.size = 0

    def empty(self):
        return len(self.cola) == 0

    def encolar(self,dato):
        self.cola += [dato]
        self.size += 1

    def desencolar(self):
        if self.empty():
            print("La cola esta vacia")
        else:
            self.cola = [self.cola[i] for i in range(1,self.size)]
            self.size -= 1

    def mostrar(self):
        n = self.size - 1
        while n > -1:
            print("[{}] => {}".format(n,self.cola[n]))
            n -= 1

# cola1 = Cola()
# cola1.encolar(4)
# cola1.encolar(5)
# cola1.encolar(7)
# cola1.desencolar()
# cola1.mostrar()
