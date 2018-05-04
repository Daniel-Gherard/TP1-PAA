#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Classe com todas as funcionalidades de grafos."""


class Grafo(object):

    def __init__(self, dicionario):
        # Inicializa o grafo com o dicionário enviado.

        self.dicionario = dicionario

    # Método para recuperar os vértices do grafo. Ou seja, as chaves do dicionário.
    def pegar_vertices(self):
        return list(self.dicionario.keys())

    # Método para recuperar as arestas do grafo.
    def pegar_arestas(self):
        todas_as_arestas = []

        for vertices in self.dicionario:
            for arestas in self.dicionario[vertices]:
                if arestas not in todas_as_arestas:
                    todas_as_arestas.append(arestas)

        return todas_as_arestas

    # Método para adicionar vértices:
    def adicionar_vertice(self, vertice):
        if vertice not in self.dicionario.keys():
            self.dicionario[vertice] = []
            return True
        else:
            return False

    # Método para adicionar arestas:
    def adicionar_aresta(self, vertice1, vertice2, peso, index):
        aresta = {"de": vertice1, "para": vertice2, "peso": peso, "index": index}

        todas_as_arestas = self.dicionario[vertice1]

        if aresta in todas_as_arestas:
            return
        else:
            self.dicionario[vertice1].append(aresta)

    # Método para encontrar o índice da aresta:
    def aresta_index(self, vertice1, vertice2):
        arestas = self.dicionario[vertice1]

        for aresta in arestas:
            if aresta["para"] == vertice2:
                return aresta["index"]

    # Método para encontrar o peso de uma aresta:
    def aresta_peso(self, vertice1, vertice2):
        arestas = self.dicionario[vertice1]

        for aresta in arestas:
            if aresta["para"] == vertice2:
                return aresta["peso"]

    # Método para encontrar todos os índices das arestas nos caminhos:
    def get_todas_as_arestas_indexes(self, caminhos, indexes, pesos):
        for caminho in caminhos:
            index = []
            peso = 0

            for x in range(0, len(caminho)):
                if x + 1 >= len(caminho):
                    break
                else:
                    j = self.aresta_index(caminho[x], caminho[x + 1])
                    k = self.aresta_peso(caminho[x], caminho[x + 1])
                    index.append(j)
                    if k is not None:
                        peso = peso + k

            indexes.append(index)
            pesos.append(peso)
