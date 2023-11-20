class pila:
    def __init__(self):
        self.items = []
        
    def empty_pila(self):
        return len(self.items) == 0
    
    def push_pila(pila, elemento):
        self.items.append(elemento)
        
    def pop_pila(pila):
        if not self.empty_pila():
            return self.items.pop()
        
        return None
    
    def peek_pila(pila):
        if not self.empty_pila():
            return pila[-1]
        
        return None