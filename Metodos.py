#Clase con métodos y atributos de una pila.
class Metodos:
    
    #Definir si el valor a evaluar es un número, letra o operador.
    letras = list ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numeros = list ('0123456789')
    
    #Atributos de una pila
    tamanio = 0 #Tamaño máximo de la pila
    pila = []  
    tope = 0  
    
    #Almacen de la expresión convertida.
    expresion_postfija = []
   
    #Constructor de la clase
    def __init__(self, tamanio, expresion_postfija):
        self.tamanio = tamanio
        self.expresion_postfija = expresion_postfija
        self.tope = -1
        self.letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.numeros = list('0123456789')

    #Define si la pila está llena
    def pila_llena(self):
        if self.tope == self.tamanio:    #Si tope = tamaño:la pila está llena.
            print("La pila esta llena")
            return True
        return False
    #Define si la pila esta vacía
    def pila_vacia(self):
        if self.tope == -1:     #Si = -1: pila esta vacía.
            return True
        return False

    #Método para apilar un valor en la pila 
    def apilar(self, dato):
        if not self.pila_llena():   #Si pila != llena:añade el dato e incrementa el tope de la pila.
            self.pila.insert(self.tope, dato)
            self.tope += 1
    
    #Método para desapilar un valor en la pila.
    def desapilar(self):
        if not self.pila_vacia():
            aux = self.pila[self.tope]
            del self.pila[self.tope]
            self.tope -= 1
            return aux
    
    #Método que define la prioridad los operadores en la expresión.
    def prioridad_operacion(self, EI, i):
        if EI[i] == '^':
            prioridadop = 4
            return prioridadop
        elif EI[i] == '*':
            prioridadop = 2
            return prioridadop
        elif EI[i] == '/':
            prioridadop = 2
            return prioridadop
        elif EI[i] == '+':
            prioridadop = 1
            return prioridadop
        elif EI[i] == '-':
            prioridadop = 1
            return prioridadop
        elif EI[i] == '(':
            prioridadop = 5
            return prioridadop

        return 0
    
    #Método que define la prioridad de los operadores en la pila.
    def prioridad_pila(self):
        if self.pila[self.tope] == '^':
            prioridadpila = 3
            return prioridadpila
        elif self.pila[self.tope] == '*':
            prioridadpila = 1
            return prioridadpila
        elif self.pila[self.tope] == '/':
            prioridadpila = 1
            return prioridadpila
        elif self.pila[self.tope] == '+':
            prioridadpila = 2
            return prioridadpila
        elif self.pila[self.tope] == '-':
            prioridadpila = 2
            return prioridadpila
        elif self.pila[self.tope] == '(':
            prioridadpila = 0
            return prioridadpila
        elif self.pila[self.tope] == ')':
            prioridadpila = 0
            return prioridadpila

        return 0
    
    #Método que define si el dato es un operador, una letra o un numero
    def es_operador(self, ei, i):
        if ei[i] in self.letras or ei[i] in self.numeros:
            return False
        return True