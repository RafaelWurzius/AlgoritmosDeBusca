import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    # Adicionar aresta com um custo entre dois nós
    def adicionar_aresta(self, origem, destino, custo):
        if origem not in self.grafo:
            self.grafo[origem] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[origem].append((destino, custo))

    # Imprimir o grafo
    def imprimir_grafo(self):
        for no in self.grafo:
            print(f"{no} -> {self.grafo[no]}")

    # Busca A* até o destino
    def busca_a_estrela(self, inicio, destino, heuristica):
        # Fila de prioridade para armazenar os nós de acordo com o custo f(n) = g(n) + h(n)
        fila_prioridade = []
        visitados = set()
        custos = {inicio: 0}  # g(n): custo do caminho do nó inicial até o nó atual
        caminhos = {inicio: None}  # Armazena o caminho percorrido até o destino

        # Adiciona o nó de início à fila de prioridade com f(n) = h(n)
        heapq.heappush(fila_prioridade, (heuristica[inicio], inicio))

        while fila_prioridade:
            # Remove o nó com menor f(n) = g(n) + h(n)
            _, no_atual = heapq.heappop(fila_prioridade)

            # Se o nó de destino for encontrado, reconstrói o caminho
            if no_atual == destino:
                caminho = []
                while no_atual is not None:
                    caminho.append(no_atual)
                    no_atual = caminhos[no_atual]
                caminho.reverse()
                print("\nNó de destino encontrado:", destino)
                print("Caminho:", " -> ".join(caminho))
                print("Custo total:", custos[destino])
                return

            visitados.add(no_atual)

            # Explora os vizinhos do nó atual
            for vizinho, custo_salto in self.grafo[no_atual]:
                if vizinho in visitados:
                    continue

                # Calcula o custo g(n) para chegar ao vizinho
                novo_custo = custos[no_atual] + custo_salto

                # Se o vizinho não tiver sido visitado ou se encontramos um caminho mais barato, atualizamos
                if vizinho not in custos or novo_custo < custos[vizinho]:
                    custos[vizinho] = novo_custo
                    f_n = novo_custo + heuristica[vizinho]  # f(n) = g(n) + h(n)
                    heapq.heappush(fila_prioridade, (f_n, vizinho))
                    caminhos[vizinho] = no_atual

        print("\nNó de destino não encontrado no grafo.")

if __name__ == "__main__":
    g = Grafo()

    # Adicionar arestas com custos
    g.adicionar_aresta('A', 'C', 1)

    g.adicionar_aresta('C', 'A', 1)
    g.adicionar_aresta('C', 'B', 1)
    g.adicionar_aresta('C', 'G', 1)

    g.adicionar_aresta('B', 'C', 1)
    g.adicionar_aresta('B', 'D', 1)

    g.adicionar_aresta('D', 'B', 1)
    g.adicionar_aresta('D', 'E', 2)

    g.adicionar_aresta('E', 'D', 1)
    g.adicionar_aresta('E', 'F', 1)
    
    g.adicionar_aresta('F', 'E', 2)
    g.adicionar_aresta('F', 'J', 1)

    g.adicionar_aresta('J', 'F', 1)
    g.adicionar_aresta('J', 'I', 1)
    g.adicionar_aresta('J', 'M', 2)

    g.adicionar_aresta('I', 'J', 1)
    g.adicionar_aresta('I', 'H', 1)

    g.adicionar_aresta('H', 'I', 1)
    g.adicionar_aresta('H', 'L', 2)
    g.adicionar_aresta('H', 'G', 1)
    g.adicionar_aresta('H', 'K', 1)

    g.adicionar_aresta('G', 'C', 1)
    g.adicionar_aresta('G', 'H', 1)
    g.adicionar_aresta('G', 'K', 1)

    g.adicionar_aresta('K', 'G', 1)
    g.adicionar_aresta('K', 'N', 2)
    g.adicionar_aresta('K', 'H', 1)
    
    g.adicionar_aresta('L', 'H', 1)
    g.adicionar_aresta('L', 'M', 2)

    g.adicionar_aresta('M', 'J', 1)
    g.adicionar_aresta('M', 'L', 2)
    g.adicionar_aresta('M', 'P', 3)

    g.adicionar_aresta('N', 'K', 1)
    g.adicionar_aresta('N', 'Q', 2)
    g.adicionar_aresta('N', 'O', 1)
    
    g.adicionar_aresta('O', 'N', 2)
    g.adicionar_aresta('O', 'P', 3)

    g.adicionar_aresta('P', 'O', 1)
    g.adicionar_aresta('P', 'M', 2)
    g.adicionar_aresta('P', 'T', 2)

    g.adicionar_aresta('Q', 'N', 2)
    g.adicionar_aresta('Q', 'R', 1)

    g.adicionar_aresta('T', 'P', 3)
    g.adicionar_aresta('T', 'S', 1)
    g.adicionar_aresta('T', 'U', 1)

    g.adicionar_aresta('U', 'T', 2)

    g.adicionar_aresta('S', 'R', 1)
    g.adicionar_aresta('S', 'T', 2)

    g.adicionar_aresta('R', 'Q', 2)
    g.adicionar_aresta('R', 'S', 1)   

    # Definição da heurística (quantidade de salas até o destino 'M')
    heuristica = {
        'A': 5,
        'B': 5,
        'C': 4,
        'D': 4,
        'E': 3,
        'F': 2,
        'G': 3,
        'H': 2,
        'I': 2,
        'J': 1,
        'K': 3,
        'L': 1,
        'M': 0,
        'N': 3,
        'O': 2,
        'P': 1,
        'Q': 4,
        'R': 4,
        'S': 3,
        'T': 2,
        'U': 3
    }

    print("Estrutura do Grafo:")
    g.imprimir_grafo()

    destino = 'M'
    print(f"\nBusca A* a partir do nó A até o nó {destino}:")
    g.busca_a_estrela('A', destino, heuristica)
