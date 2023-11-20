class cola:
    def __init__(self):
        self.items = []
        
    def empty_cola(self):
        return len(self.items) == 0
    
    def enqueue_cola(self, elemento):
        self.items.append(elemento)
        
    def dequeue_cola(pila):
        if not self.esta_vacia():
            return self.items.pop(0)
        
        return None
    
    def peek_cola(self):
        if not self.esta_vacia():
            return self.items[0]
        
        return None