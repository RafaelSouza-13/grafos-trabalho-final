from grafo import GrafoDirecionado
from algoritmos import FordFulkerson

g = GrafoDirecionado(6)
g.adiciona_aresta(0, 1, 16)
g.adiciona_aresta(0, 2, 13)
g.adiciona_aresta(1, 2, 10)
g.adiciona_aresta(1, 3, 12)
g.adiciona_aresta(2, 1, 4)
g.adiciona_aresta(2, 4, 14)
g.adiciona_aresta(3, 2, 9)
g.adiciona_aresta(3, 5, 20)
g.adiciona_aresta(4, 3, 7)
g.adiciona_aresta(4, 5, 4)


origem = 0
destino = 5

ford_fulkerson = FordFulkerson(g)
fluxo_maximo = ford_fulkerson.executar(origem, destino)

print(f"Fluxo máximo: {fluxo_maximo}")

