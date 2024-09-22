import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    # Adicionar aresta entre dois nós
    def adicionar_aresta(self, origem, destino):
        if origem not in self.grafo:
            self.grafo[origem] = []
        if destino not in self.grafo:
            self.grafo[destino] = []
        self.grafo[origem].append(destino)

    # Imprimir o grafo
    def imprimir_grafo(self):
        for no in self.grafo:
            print(f"{no} -> {self.grafo[no]}")

    # Busca Gulosa (Greedy) até o destino, com base em uma heurística
    def busca_gulosa_ate_destino(self, inicio, destino, heuristica):
        # Fila de prioridade para armazenar os nós de acordo com a heurística
        fila_prioridade = []
        visitados = set()

        # Adiciona o nó de início à fila de prioridade com base na heurística
        heapq.heappush(fila_prioridade, (heuristica[inicio], inicio))

        while fila_prioridade:
            _, no_atual = heapq.heappop(fila_prioridade)  # Remove o nó com menor valor heurístico

            # Printa o nó atual
            print(no_atual, end=" ")

            # Se o nó de destino for encontrado, interrompe a busca
            if no_atual == destino:
                print("\nNó de destino encontrado:", destino)
                return

            visitados.add(no_atual)

            # Adiciona os vizinhos do nó atual à fila de prioridade
            for vizinho in self.grafo[no_atual]:
                if vizinho not in visitados:
                    heapq.heappush(fila_prioridade, (heuristica[vizinho], vizinho))

        print("\nNó de destino não encontrado no grafo.")

if __name__ == "__main__":
    g = Grafo()

    # Adicionar arestas
    g.adicionar_aresta('A', 'C')

    g.adicionar_aresta('C', 'A')
    g.adicionar_aresta('C', 'B')
    g.adicionar_aresta('C', 'G')

    g.adicionar_aresta('B', 'C')
    g.adicionar_aresta('B', 'D')

    g.adicionar_aresta('D', 'B')
    g.adicionar_aresta('D', 'E')

    g.adicionar_aresta('E', 'D')
    g.adicionar_aresta('E', 'F')
    
    g.adicionar_aresta('F', 'E')
    g.adicionar_aresta('F', 'J')

    g.adicionar_aresta('J', 'F')
    g.adicionar_aresta('J', 'I')
    g.adicionar_aresta('J', 'M')

    g.adicionar_aresta('I', 'J')
    g.adicionar_aresta('I', 'H')

    g.adicionar_aresta('H', 'I')
    g.adicionar_aresta('H', 'L')
    g.adicionar_aresta('H', 'G')
    g.adicionar_aresta('H', 'K')

    g.adicionar_aresta('G', 'C')
    g.adicionar_aresta('G', 'H')
    g.adicionar_aresta('G', 'K')

    g.adicionar_aresta('K', 'G')
    g.adicionar_aresta('K', 'N')
    g.adicionar_aresta('K', 'H')
    
    g.adicionar_aresta('L', 'H')
    g.adicionar_aresta('L', 'M')

    g.adicionar_aresta('M', 'J')
    g.adicionar_aresta('M', 'L')
    g.adicionar_aresta('M', 'P')

    g.adicionar_aresta('N', 'K')
    g.adicionar_aresta('N', 'Q')
    g.adicionar_aresta('N', 'O')
    
    g.adicionar_aresta('O', 'N')
    g.adicionar_aresta('O', 'P')

    g.adicionar_aresta('P', 'O')
    g.adicionar_aresta('P', 'M')
    g.adicionar_aresta('P', 'T')

    g.adicionar_aresta('Q', 'N')
    g.adicionar_aresta('Q', 'R')

    g.adicionar_aresta('T', 'P')
    g.adicionar_aresta('T', 'S')
    g.adicionar_aresta('T', 'U')

    g.adicionar_aresta('U', 'T')

    g.adicionar_aresta('S', 'R')
    g.adicionar_aresta('S', 'T')

    g.adicionar_aresta('R', 'Q')
    g.adicionar_aresta('R', 'S')

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

    inicio = 'A'
    destino = 'M'
    print(f"\nBusca Gulosa a partir do nó {inicio} até o nó {destino}:")
    g.busca_gulosa_ate_destino(inicio, destino, heuristica)
