from collections import deque

class Grafo:
    def __init__(self):
        self.grafo = {}

    # Adicionar aresta entre dois nós (direcionada ou não direcionada)
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

    # Busca em Largura (BFS) até encontrar o nó de destino
    def busca_largura_ate_destino(self, inicio, destino):
        visitados = set()  # Conjunto para marcar nós visitados
        fila = deque([inicio])  # Fila para o BFS, começando pelo nó de origem
        visitados.add(inicio)

        while fila:
            no_atual = fila.popleft()  # Remove o primeiro nó da fila
            print(no_atual, end=" ")  # Processa o nó (neste caso, apenas imprime)

            # Se encontramos o nó de destino, encerramos a busca
            if no_atual == destino:
                print("\nNó de destino encontrado:", destino)
                return

            # Adiciona os vizinhos do nó atual que ainda não foram visitados
            for vizinho in self.grafo[no_atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    visitados.add(vizinho)

        print("\nNó de destino não encontrado no grafo.")

# Exemplo de uso
if __name__ == "__main__":
    g = Grafo()

    # Adicionar algumas arestas
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


    # Imprimir o grafo
    print("Estrutura do Grafo:")
    g.imprimir_grafo()

    # Realizar a busca em largura até encontrar o nó de destino
    inicio = 'A'
    destino = 'E'

    print(f"\nBusca em Largura a partir do nó A até o nó {destino}:")
    g.busca_largura_ate_destino(inicio, destino)
