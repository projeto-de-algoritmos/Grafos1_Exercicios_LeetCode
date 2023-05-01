class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        
        # Função dfs que calcula a probabilidade do sapo estar no nó target
        def dfs(no, tempo, prob):
            
            # Variável probabilidade foi definida como nonlocal, pois a dfs realiza chamadas recursivas
            nonlocal probabilidade
            vizinhos = grafo[no]
            nosNaoVisitados = [v for v in vizinhos if v not in nosVisitados]

            # Prevenção para que a execução não exceda o tempo limite
            if tempo > t:
                return
            
            if no == target:
                if tempo == t or not nosNaoVisitados:
                    probabilidade = prob
                return
            
            # Calculando a probabilidade de acordo com a quantidade de vizinhos não visitados
            if nosNaoVisitados:
                p = 1 / len(nosNaoVisitados)
            
            # Fazendo a função visitar um nó apenas uma vez, evitando que a função fique em um loop infinito 
            for v in nosNaoVisitados:
                nosVisitados.add(v)
                dfs(v, tempo + 1, prob * p)
                nosVisitados.remove(v)
        
        # Criando a estrutura grafo de acordo com as arestas passadas
        grafo = defaultdict(list)
        for a, b in edges:
            grafo[a].append(b)
            grafo[b].append(a)
    
        nosVisitados = set()
        nosVisitados.add(1)
        probabilidade = 0

        # Chamando a dfs a partir do nó 1, com tempo inicial de 0 segundos e probabilidade inicial de 1 (100%)
        dfs(1, 0, 1)

        return probabilidade