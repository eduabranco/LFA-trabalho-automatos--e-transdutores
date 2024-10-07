from graphviz import Digraph

class MaquinaDeRefrigerante:
    def __init__(self):
        self.estado = 0  # O estado inicial é 0 centavos

    def inserir_moeda(self, moeda):
        if moeda not in [25, 50, 100]:
            raise ValueError("Moeda inválida. Insira 25, 50 ou 100 centavos.")

        # Atualiza o estado somando o valor da moeda inserida
        self.estado += moeda

        if self.estado >= 100:
            # Se o valor total for maior ou igual a 1 real (100 centavos), libera uma lata
            self.estado -= 100  # Subtrai 1 real do estado
            return 1  # Lata liberada
        else:
            # Caso contrário, ainda não atinge 1 real, não libera a lata
            return 0  # Lata não liberada
        
    def criar_grafico():
        fsm = Digraph('MealyMachine', format='png')
        
        # Definindo os estados
        fsm.attr('node', shape='circle')
        fsm.node('S0', '0')  # Estado inicial, acumulado = 0
        fsm.node('S25', '25')  # Acumulado = 25
        fsm.node('S50', '50')  # Acumulado = 50
        fsm.node('S75', '75')  # Acumulado = 75
        fsm.node('S100', '100')  # Acumulado = 100 ou mais
        
        # Definindo as transições e as saídas (formato: entrada / saída)
        # Do estado S0
        fsm.edge('S0', 'S25', label='25 / 0')  # Inserir 25 centavos
        fsm.edge('S0', 'S50', label='50 / 0')  # Inserir 50 centavos
        fsm.edge('S0', 'S0', label='100 / 1')  # Inserir 1 real
        
        # Do estado S25
        fsm.edge('S25', 'S50', label='25 / 0')  # Inserir 25 centavos
        fsm.edge('S25', 'S75', label='50 / 0')  # Inserir 50 centavos
        fsm.edge('S25', 'S25', label='100 / 1')  # Inserir 1 real
        
        # Do estado S50
        fsm.edge('S50', 'S75', label='25 / 0')  # Inserir 25 centavos
        fsm.edge('S50', 'S100', label='50 / 1')  # Inserir 50 centavos
        fsm.edge('S50', 'S50', label='100 / 1')  # Inserir 1 real
        
        # Do estado S75
        fsm.edge('S75', 'S100', label='25 / 1')  # Inserir 25 centavos
        fsm.edge('S75', 'S25', label='50 / 1')  # Inserir 50 centavos
        fsm.edge('S75', 'S100', label='100 / 1')  # Inserir 1 real
        
        # Do estado S100 (transições recursivas com saída 1)
        fsm.edge('S100', 'S25', label='25 / 0')  # Inserir 25 centavos após liberar uma lata
        fsm.edge('S100', 'S50', label='50 / 0')  # Inserir 50 centavos após liberar uma lata
        fsm.edge('S100', 'S100', label='100 / 1')  # Inserir 1 real após liberar uma lata
        
        return fsm

# Exemplo de uso
maquina = MaquinaDeRefrigerante()

# Simulação da inserção de moedas
moedas = [25, 50, 25, 100]  # Sequência de moedas inseridas
saidas = [maquina.inserir_moeda(moeda) for moeda in moedas]

print(saidas)  # Saída será: [0, 0, 1, 1] (a primeira lata sai após 1 real e a outra após o próximo real)



# Gerar e visualizar o gráfico da máquina de Mealy
mealy_machine = maquina.criar_grafico()
mealy_machine.render(filename='mealy_machine', directory='C:\\user\\Downloads\\q3', format='png') 