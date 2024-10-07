from graphviz import Digraph

# Função para gerar o autômato finito determinístico (DFA) usando Graphviz
def gerar_automato(nome, transicoes, estado_inicial, estados_finais):
    dfa = Digraph(nome)
    
    # Configuração de estados finais (duplo círculo)
    for estado in estados_finais:
        dfa.node(str(estado), shape='doublecircle')
    
    # Configuração de estados normais
    for estado in transicoes.keys():
        if estado not in estados_finais:
            dfa.node(str(estado), shape='circle')

    # Criação das transições
    for estado_origem, arestas in transicoes.items():
        for simbolo, estado_destino in arestas.items():
            dfa.edge(str(estado_origem), str(estado_destino), label=simbolo)
    
    # Estado inicial
    dfa.node('ini', shape='point')  # Ponto que representa o início
    dfa.edge('ini', str(estado_inicial))  # Transição para o estado inicial
    return dfa.render(directory="C:\\user\\Downloads\\q1",format="png")

# Implementando cada autômato conforme as expressões regulares

# 1. (ab*c*)*
transicoes_1 = {
    0: {'a': 1},  # Estado inicial
    1: {'b': 1, 'c': 2, 'a': 1},
    2: {'c': 2, 'a': 1},
}
estado_inicial_1 = 0
estados_finais_1 = [0, 1, 2]

# 2. aaa(b | c)* | (b | c)* aaa
transicoes_2 = {
    0: {'a': 1, 'b': 4, 'c': 4},
    1: {'a': 2},
    2: {'a': 3},
    3: {'b': 3, 'c': 3},  # aaa(b|c)*
    4: {'b': 4, 'c': 4, 'a': 5},  # (b|c)*aaa
    5: {'a': 6},
    6: {'a': 3}
}
estado_inicial_2 = 0
estados_finais_2 = [3]

# 3. a*b | ab*
transicoes_3 = {
    0: {'a': 1, 'b': 2},
    1: {'a': 1, 'b': 3},
    2: {},
    3: {'b': 3}
}
estado_inicial_3 = 0
estados_finais_3 = [2, 3]

# 4. a*b* (a | ac*)
transicoes_4 = {
    0: {'a': 1, 'b': 2},
    1: {'a': 1, 'b': 2, 'a': 3},
    2: {'a': 3},
    3: {'c': 3}
}
estado_inicial_4 = 0
estados_finais_4 = [2, 3]

# Gerando os autômatos
dfa_1 = gerar_automato("DFA_1", transicoes_1, estado_inicial_1, estados_finais_1)
dfa_2 = gerar_automato("DFA_2", transicoes_2, estado_inicial_2, estados_finais_2)
dfa_3 = gerar_automato("DFA_3", transicoes_3, estado_inicial_3, estados_finais_3)
dfa_4 = gerar_automato("DFA_4", transicoes_4, estado_inicial_4, estados_finais_4)

# Exibindo os autômatos
dfa_1, dfa_2, dfa_3, dfa_4

