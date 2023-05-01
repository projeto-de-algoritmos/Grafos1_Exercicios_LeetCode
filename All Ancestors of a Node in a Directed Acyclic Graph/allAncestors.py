from collections import defaultdict
from collections import deque
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        #O resultado é retornado como uma lista de listas, onde a i-ésima lista contém os ancestrais do nó i.
        adjList = defaultdict(list) # cria a lista de adjacencia
        grau = defaultdict(int) # cria o auxiliar que irá guardar o grau de entrada de cada nó
        # Itera sobre as arestas do grafo e adiciona cada aresta à lista de adjacência correspondente ao pai.
        for pai, filho in edges:
            adjList[pai].append(filho)
            grau[filho] += 1 
        
        fila = deque([node for node in range(n) if node not in grau]) # cria uma fila com todos os nos que não tem arestas chegando
        resultado = [set() for _ in range(n)]
        # itera sobre a fila e atualiza a lista de ancestrais para todos os nós filhos do nó atual. A fila é atualizada com os nós que não tem mais arestas de entrada.
        while fila:
            node = fila.popleft()
            for child in adjList[node]:
                resultado[child].add(node)
                resultado[child].update(resultado[node])
                grau[child] -= 1
                if grau[child] == 0:
                    fila.append(child)
        return [sorted(x) for x in resultado] # Retorna a lista de ancestrais para cada nó no grafo, ordenando cada uma das listas antes de retornar o resultado

        ### Outra lógica que também solucionaria esse problema, seria gerar o grafo reverso da DAG e rodar uma DFS para todos os nós do Grafo reverso e ir armazenando numa lista de listas, e ,ao final, ordenar essa lista que será retorna conforme o enunciado pede.
