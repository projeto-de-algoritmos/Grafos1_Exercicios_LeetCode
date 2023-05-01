class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        vetor = [-1]*N  #criando um array preenchido inicialmente com -1 para represetar os nós não pintados

        fila = deque() # cria a fila
        fila.append((0,0)) # marca o primeiro nó como 0
        #bfs
        while fila: # enquanto tivermos uma fila
            node, cor = fila.popleft() #retiro da fila
            if vetor[node] == -1: # se ainda não tiver sido pintado, passo para a fila todos os adjacentes e sigo por camadas
                vetor[node] = cor
                for proximos in graph[node]:
                    fila.append((proximos,cor^1))
            if vetor[node] != cor:
                return False
        return True