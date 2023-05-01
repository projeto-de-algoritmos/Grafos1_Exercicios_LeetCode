class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # Função para realizar uma busca em profundidade a partir de um nó, atualizando as profundidades dos nós visitados e calculando ciclos no grafo.
        def dfs(node, visited, curr_depth):
            # Marca o nó como visitado e atualiza a profundidade dele.
            visited[node] = True
            depth[node] = curr_depth
            # Visita todos os vizinhos do nó.
            for neighbor in graph[node]:
                # Se o vizinho ainda não foi visitado, chama a função dfs
                # recursivamente para ele.
                if not visited[neighbor]:
                    dfs(neighbor, visited, curr_depth + 1)
                # Se o vizinho já foi visitado, calcula o comprimento do ciclo
                # entre o nó atual e o vizinho.
                else:
                    cycle = curr_depth - depth[neighbor] + 1
                    nonlocal max_cycle
                    # Se o ciclo tem comprimento maior que 1, atualiza o comprimento máximo de ciclo encontrado.
                    if cycle > 1:
                        max_cycle = max(max_cycle, cycle)
                    # Se o ciclo tem comprimento igual a -1, significa que o vizinho já foi visitado em uma busca anterior a partir de outro nó, e portanto não pode fazer parte de um ciclo que comece a partir do nó atual.
                    elif cycle == -1:
                        max_cycle = -1
            # Desmarca o nó como visitado, para permitir que ele seja visitado em buscas futuras a partir de outros nós.
            visited[node] = False

        # Inicializa o comprimento máximo de ciclo encontrado como -1.
        max_cycle = -1
        # Calcula o número total de nós no grafo (assumindo que os nós são numerados a partir de 0 até o valor máximo encontrado na lista de arestas).
        n = max(edges) + 1
        # Cria uma lista de adjacências para cada nó do grafo.
        graph = [[] for _ in range(n)]
        # Cria uma lista para armazenar as profundidades de cada nó.
        depth = [-1] * n
        # Adiciona as arestas do grafo na lista de adjacências.
        for u, v in zip(edges[:-1], edges[1:]):
            graph[u].append(v)
        # Faz uma busca em profundidade a partir de cada nó do grafo, para
        # encontrar ciclos que começam em cada nó.
        for start in range(n):
            visited = [False] * n
            curr_depth = 1
            dfs(start, visited, curr_depth)
        # Retorna o comprimento máximo de ciclo encontrado no grafo.
        return max_cycle