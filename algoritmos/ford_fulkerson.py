class FordFulkerson:
    def __init__(self, grafo):
        self.grafo = grafo

    def executar(self, fonte, sumidouro):
        pai = [-1] * self.grafo.total_vertices
        fluxo_maximo = 0

        while self.dfs(fonte, sumidouro, pai):
            fluxo_caminho = float("Inf")
            v = sumidouro

            while v != fonte:
                u = pai[v]
                fluxo_caminho = min(fluxo_caminho, self.grafo.matriz_adjacencia[u][v])
                v = u
            v = sumidouro

            while v != fonte:
                u = pai[v]
                self.grafo.matriz_adjacencia[u][v] -= fluxo_caminho
                self.grafo.matriz_adjacencia[v][u] += fluxo_caminho
                v = u
            fluxo_maximo += fluxo_caminho

        return fluxo_maximo

    def dfs(self, fonte, sumidouro, pai):
        visitado = [False] * self.grafo.total_vertices
        pilha = [fonte]

        while pilha:
            u = pilha.pop()

            for v in range(self.grafo.total_vertices):
                if not visitado[v] and self.grafo.matriz_adjacencia[u][v] > 0:
                    pilha.append(v)
                    pai[v] = u
                    visitado[v] = True
                    if v == sumidouro:
                        return True
        return False
