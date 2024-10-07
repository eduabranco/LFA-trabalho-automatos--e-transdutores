import graphviz

# Função para criar o autômato finito determinístico para a palavra "computador"
def create_automaton():
    automaton = graphviz.Digraph(format='png')
    word = "computador"

    # Adiciona estados e transições ao autômato
    for i in range(len(word) + 1):
        automaton.node(str(i), shape="circle")

    # Adiciona transições entre os estados
    for i in range(len(word)):
        automaton.edge(str(i), str(i+1), label=word[i])

    # Estado final é o de aceitação
    automaton.node(str(len(word)), shape="doublecircle")

    return automaton

# Função que implementa o automato para encontrar a palavra "computador" no texto
def find_word_positions(text, word):
    positions = []
    word_len = len(word)
    
    # Percorre o texto para verificar as ocorrências da palavra
    for i in range(len(text) - word_len + 1):
        if text[i:i + word_len].lower() == word:
            positions.append(i)
    
    return positions

# Texto fornecido
T = """O computador é uma máquina capaz de variados tipos de tratamento automático de
informações ou processamento de dados. Entende-se por computador um sistema físico que
realiza algum tipo de computação. Assumiu-se que os computadores pessoais e laptops são
ícones da era da informação. O primeiro computador eletromecânico foi construído por
Konrad Zuse (1910–1995). Atualmente, um microcomputador é também chamado
computador pessoal ou ainda computador doméstico."""

# Palavra que o autômato deve encontrar
word = "computador"

# Cria o autômato e salva o desenho
automaton = create_automaton()
automaton.render(filename='automaton', directory="C:\\user\\Downloads\\q2",format="png")

# Busca pelas posições da palavra no texto
positions = find_word_positions(T, word)

# Mostra as posições encontradas
print(f"A palavra '{word}' ocorre nas posições: {positions}")
