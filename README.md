# Comparação de Algoritmos de Busca 🔎

Este repositório contém implementações em **Python** de quatro algoritmos de busca aplicados ao mesmo problema:  

- **Busca em Largura (BFS)**
- **Busca em Profundidade (DFS)**
- **Busca Gulosa**
- **Busca A\***  

---

## 📖 Diferença entre os algoritmos

### 🔹 Busca em Largura (BFS - Breadth-First Search)
- Explora os nós **nível por nível**, visitando todos os vizinhos antes de avançar.
- Garante encontrar a **solução ótima** (menor caminho em número de passos), se existir.
- Pode ser **custosa em memória**, pois precisa armazenar todos os nós de um nível antes de avançar.

### 🔹 Busca em Profundidade (DFS - Depth-First Search)
- Explora sempre o **caminho mais profundo** antes de retroceder (backtracking).
- Usa menos memória que a BFS.
- **Não garante a solução ótima**, e em alguns casos pode não encontrar solução se ficar presa em caminhos infinitos.

### 🔹 Busca Gulosa (Greedy Best-First Search)
- Sempre escolhe expandir o nó que parece estar **mais próximo do objetivo**, baseado em uma **função heurística h(n)**.
- Mais rápida que BFS/DFS em muitos casos.
- **Não garante solução ótima** – pode se desviar do melhor caminho.

### 🔹 Busca A\* (A-Star)
- Combina o custo real do caminho até o nó (**g(n)**) com a estimativa heurística até o objetivo (**h(n)**).
- Função de avaliação:  
  **f(n) = g(n) + h(n)**
- **Garante a solução ótima** se a heurística for admissível (nunca superestima o custo).
- Geralmente mais eficiente que BFS em problemas com heurísticas boas.

---
## ⚙️ Execução

Cada algoritmo deve ser executado individualmente.  

```bash
python aEstrela.py
```

```bash
python buscaEmLargura.py
```

```bash
python buscaEmProfundidade.py
```

```bash
python buscaGulosa.py
```


## Explicação dos algorimos
https://drive.google.com/file/d/1IDezft0EX_kpfDjHIdSYDUpuaa9xrOud/view?usp=sharing 
