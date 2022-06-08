class Nodo:
    def __init__(self,valor_):
        self.valor= valor_
        self.siguiente = None
        self.anterior = None


class Lista_doblementecircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None        

    def agregar(self,valor_):
        nuevo = Nodo(valor_)
        if(self.primero == None):    
            self.primero = nuevo
        else:
            nuevo.anterior = self.ultimo            
            self.ultimo.siguiente = nuevo
        self.ultimo = nuevo
        self.ultimo.siguiente = self.primero
        self.primero.anterior = self.ultimo

    def imprimir(self):
        aux = self.primero
        while aux != None:
            print('anterior: '+str(aux.anterior.valor)+' valor a: '+str(aux.valor) + ' valor sig: '+str(aux.siguiente.valor))
            if (aux.siguiente == self.primero):
                return
            aux = aux.siguiente

lis = Lista_doblementecircular()
x = int(input('Ingrese el tamaño de la lista: \n'))
print('Ingrese los datos de la lista')
for i in range(1,x+1):
    y = input()
    lis.agregar(y)

lis.imprimir()