import numpy as np
import matplotlib.pyplot as plt
from grafo.vertice import Vertice

class Grafo:
    def __init__(self, numero_vertices=0):
        self.total_vertices = numero_vertices
        self.vertices = self.inicia_vertices(numero_vertices)
        self.matriz_adjacencia = self.inicializa_matrix_adjacencia(numero_vertices)

    def inicia_vertices(self, numero_vertices):
        vertices = []
        for i in range(numero_vertices):
            vertice = Vertice(i)
            vertices.append(vertice)
        return vertices

    def inicializa_matrix_adjacencia(self, numero_vertices):
        return np.zeros((numero_vertices, numero_vertices), dtype=np.int32)

    def exibe_vertices(self):
        print("Vértices: {", end="")
        for vertice in self.vertices:
            print(vertice.id, end=", ")
        print("}")

    def adiciona_aresta(self, u, v, capacidade):
        self.matriz_adjacencia[u][v] = capacidade

    def exibe_matriz(self):
        fig, ax = plt.subplots()
        cax = ax.imshow(self.matriz_adjacencia, cmap='Spectral', interpolation='nearest')

        fig.colorbar(cax)

        ax.set_title('Matriz de Adjacências')
        ax.set_xlabel('Vértices Adjacentes')
        ax.set_ylabel('Vértices')

        for i in range(self.matriz_adjacencia.shape[0]):
            for j in range(self.matriz_adjacencia.shape[1]):
                ax.text(j, i, str(self.matriz_adjacencia[i, j]),
                        ha='center', va='center',
                        color='white')

        ax.set_xticks(np.arange(self.matriz_adjacencia.shape[1]))
        ax.set_yticks(np.arange(self.matriz_adjacencia.shape[0]))
        ax.set_xticklabels(np.arange(self.matriz_adjacencia.shape[1]))
        ax.set_yticklabels(np.arange(self.matriz_adjacencia.shape[0]))

        plt.show()
