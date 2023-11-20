from collections import deque

class Banco:
    def __init__(self):
        self.cola_clientes = deque()

    def llegada_cliente(self, cliente):
        self.cola_clientes.append(cliente)
        print(f'Cliente {cliente} llegó y se unió a la cola.')

    def atender_cliente(self):
        if not self.cola_clientes:
            print('La cola de clientes está vacía. No hay clientes para atender.')
        else:
            cliente_atendido = self.cola_clientes.popleft()
            print(f'Cliente {cliente_atendido} fue atendido.')

    def mostrar_cola(self):
        if not self.cola_clientes:
            print('La cola de clientes está vacía.')
        else:
            print('Cola de clientes:')
            for cliente in self.cola_clientes:
                print(f'- {cliente}')

banco = Banco()

banco.llegada_cliente("Cliente1")
banco.llegada_cliente("Cliente2")
banco.llegada_cliente("Cliente3")

banco.mostrar_cola()

banco.atender_cliente()
banco.atender_cliente()

banco.mostrar_cola()
