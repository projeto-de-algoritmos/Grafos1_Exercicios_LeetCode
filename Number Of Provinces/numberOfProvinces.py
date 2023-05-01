class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Será implementado uma BFS e a cada vez que a fila estiver vazia, sair do while e não ainda não tiver visitado todos os nós. Significa que a componente foi explorada por completo, portanto será incrementado 1 na quantidade de componentes
        
        numComponentes = 0
        numNos = len(isConnected)
        fila = []

        # Inicializando array de tamanho numNos e com todos os valores False
        nosExplorados = [False] * numNos
        
    # Execução da BFS:

        # Passando por todos os nós do grafo que ainda não foram explorados
        for i in range(numNos):
            if not nosExplorados[i]:
                numComponentes += 1
                fila.append(i)
                while fila:
                    no = fila.pop()
                    # Marcando o nó como visitado
                    nosExplorados[no] = True
                    for j in range(numNos):
                        if isConnected[no][j] == 1 and nosExplorados[j] == False:
                            fila.append(j)
        return numComponentes
