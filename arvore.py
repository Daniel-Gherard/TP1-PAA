#!/usr/bin/python
# -*- coding: utf-8 -*-

def busca_em_profundidade(grafo, inicio, fim, todos_os_caminhos, caminho=None):
    if caminho is None:
        caminho = []
    caminho = caminho + [inicio]

    if inicio == fim:
        todos_os_caminhos.append(caminho)

    for vertice in grafo.dicionario[inicio]:
        prox_vertice = vertice["para"]

        if prox_vertice not in caminho:
            busca_em_profundidade(grafo, prox_vertice, fim, todos_os_caminhos, caminho)


def busca_em_profundidade_iterativo(grafo, inicio, fim, todos_os_caminhos, caminho=None):
    pilha = [{"pais": [], "filho": inicio}]
    caminho = []

    while pilha:
        item_da_pilha = pilha.pop()
        pais, vertice = item_da_pilha["pais"], item_da_pilha["filho"]

        if vertice is fim:
            caminho_final = list(pais)
            caminho_final.append(vertice)
            todos_os_caminhos.append(caminho_final)
            caminho = []
            continue
        else:
            for pai in pais:
                if pai not in caminho and pai is not None:
                    caminho.append(pai)

            if vertice in caminho:
                continue
            caminho.append(vertice)

            for vizinho in grafo.dicionario[vertice]:
                if vizinho not in pais:
                    v = vizinho["para"]
                    parents = list(pais)
                    parents.append(vertice)

                    pilha.append({"pais": parents, "filho": v})

    return todos_os_caminhos
