class Nodo(object):
    info,sig = None, None

class Pila(object):
    def __init__(self):
        self.tamaño = 0
        self.tope = None

    def apilar(pila, item):
        nodo = Nodo()
        nodo.info = item
        nodo.sig = pila.tope
        pila.tope = nodo
        pila.tamaño += 1
 
    def desapilar(pila):
        x = pila.tope.info
        pila.tope = pila.tope.sig
        pila.tamaño -= 1
        return x
    
    def estaVacia(pila):
        return pila.tope is None

    def mostrarTope(pila):
       if  pila.tope is not None:
        return pila.tope.info
       else:
        return None
    
    def mostrarTamaño(pila):
        return pila.tamaño
    
    def barrido(pila):
        nodo = Pila()
        while(not pila.estaVacia()):
            dato = pila.desapilar()
            print(dato)
            nodo.apilar(dato)
        while(not nodo.estaVacia()):
            dato = nodo.desapilar()
            pila.apilar(dato)


def ordenar(discIni,discFin, primero, auxiliar, ultimo):
    if discIni >= discFin:   
        if discIni % 2 == 0:
            if discFin % 2 == 0:
                ultimo.apilar(primero.desapilar())
                ordenar(discFin-1, 1, auxiliar, primero, ultimo)
            else:
                auxiliar.apilar(primero.desapilar())   
                ordenar(discFin-1, 1, ultimo, primero, auxiliar) 
        else:
            if discFin % 2 == 0:
                auxiliar.apilar(primero.desapilar())
                ordenar(discFin-1, 1, ultimo, primero, auxiliar)
            else:
                ultimo.apilar(primero.desapilar())  
                ordenar(discFin-1, 1, auxiliar, primero, ultimo)
        ordenar(discIni, discFin+1, primero, auxiliar, ultimo)

def hanoi(primero, auxiliar, ultimo):
    ordenar(primero.mostrarTamaño(),1,primero, auxiliar, ultimo)