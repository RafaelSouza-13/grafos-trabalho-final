from grafo.grafo import Grafo
import networkx as nx
import matplotlib.pyplot as plt

class GrafoDirecionado(Grafo):

    def __init__(self, numero_vertices=0, conteudo=None):
        super().__init__(numero_vertices)
        self.conteudo = conteudo

    def adiciona_aresta(self, id_vertice, id_vizinho, peso=0):
        vertice = list(filter(lambda x: x.id == id_vertice, self.vertices))
        vizinho = list(filter(lambda x: x.id == id_vizinho, self.vertices))
        if vertice:
            if vizinho:
                vertice[0].adiciona_adjacente(vizinho[0], peso)
                self.matriz_adjacencia[int(id_vertice)][int(id_vizinho)] = peso
            else:
                raise ValueError(f"Vizinho com id {id_vizinho} não encontrado.")
        else:
            raise ValueError(f"Vértice com id {id_vertice} não encontrado.")

    def exibe_arestas(self):
        print("arestas: {", end="")
        for vertice in self.vertices:
            for adjacente in vertice.adjacentes:
                print(f"{vertice} -> {adjacente})", end=",")
        print("}")
