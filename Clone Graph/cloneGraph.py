"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Se for um grafo vazio, retorna uma lista vazia
        if not node:
            return None
        else:
            # Se não for um grafo vazio, é criado uma nova lista com o grafo clonado
            grafoClonado = {}
            noClonado = Node(node.val)
            grafoClonado[node] = noClonado
        
            # A fila é usada para clonar os nós restantes
            fila = [node]
        
            # Loop para executar enquanto a fila não estiver vazia
            while fila:
                noAtual = fila.pop(0)
                noAtualClonado = grafoClonado[noAtual]

                # Clonando e adicionando os vizinhos do nó em questão no grafo clonado 
                for vizinho in noAtual.neighbors:
                    if vizinho not in grafoClonado:
                        vizinhoClonado = Node(vizinho.val)
                        grafoClonado[vizinho] = vizinhoClonado
                        fila.append(vizinho)
                    else:
                        vizinhoClonado = grafoClonado[vizinho]
            
                    noAtualClonado.neighbors.append(vizinhoClonado)

            return noClonado