#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import grafos


# Função para leitura e verificação do arquivo de entrada1.
def abrir_arquivo_entrada():
    try:
        arquivo = open(sys.argv[1], "r")
        return arquivo
    except:
        print("Arquivo não encontrado. Verifique o nome do arquivo e sua localização.\n")
	exit(1)


# Função para verificar os argumentos ao iniciar o programa. Argv.
def verificar_argumentos(argv):
    if len(argv) < 2:
        print("Não foram encontrados todos os parâmetros. O programa deve ser executado da seguinte forma:\n")
        print("./executar.sh entrada1 saida \n")
        exit(1)


# Função para popular o grafo com o arquivo de entrada1.
def ler_arquivo_e_popular_grafo(arquivo_entrada, dicionario, m, n):
    graph = grafos.Grafo(dicionario)

    with arquivo_entrada as todas_as_linhas:
        index = 0

        for linha in todas_as_linhas:
            linha = linha.split(" ")

            if len(linha) > 2:
                index += 1

                graph.adicionar_vertice(int(linha[0]))
                graph.adicionar_vertice(int(linha[1]))
                graph.adicionar_aresta(int(linha[0]), int(linha[1]), int(linha[2]), index)
            else:
                graph.n = int(linha[0])
                graph.m = int(linha[1])
                # print("Número de locais onde o acesso da imprensa é proibido: " + linha[0])
                # print("Número de corredores onde o acesso da impresa é permitido: " + linha[1])

    return graph


# Método para imprimir o arquivo de saída.
def imprimir_arquivo_de_saida(arquivo_saida, arestas, pesos):
    saida = open(arquivo_saida, "w")

    if len(pesos) > 0:
        menor_peso = min(pesos)
    else:
        menor_peso = 0

    manter = []

    # Remoção dos caminhos que não são mínimos:
    for i in range(0, len(pesos)):
        if pesos[i] == menor_peso:
            manter.append(i)

    min_arestas = []

    for m in manter:
        min_arestas.append(arestas[m])

    arestas = list(min_arestas)

    # Detecção dos 'pontos críticos' do caminho, ou seja, os pontos que, obrigatoriamente, serão percorridos.
    arestas_em_comum = []

    if len(arestas) > 1:
        for i in range(0, len(arestas)):
            if i + 1 >= len(arestas):
                break
            else:
                if len(arestas_em_comum) > 0:
                    arestas_em_comum = list(
                        set(arestas_em_comum).intersection(list(set(arestas[i]).intersection(arestas[i + 1]))))
                else:
                    arestas_em_comum = list(set(arestas[i]).intersection(arestas[i + 1]))
    else:
        for aresta in arestas:
            for a in aresta:
                arestas_em_comum.append(a)

    # Detecção de todos os indicadores dos corredores que possivelmente poderiam ser utilizados por atletas.
    corredores_possiveis = []

    for aresta in arestas:
        for index in aresta:
            if index not in corredores_possiveis:
                corredores_possiveis.append(index)

    saida.write(str(len(corredores_possiveis)) + '\n')
    corredores_possiveis.sort()

    saida.write(" ".join(str(x) for x in corredores_possiveis) + '\n')

    saida.write(str(len(arestas_em_comum)) + '\n')
    arestas_em_comum.sort()
    saida.write(" ".join(str(x) for x in arestas_em_comum) + '\n')

    saida.close()
