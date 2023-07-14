import random

import numpy as np

from AlgoritmoGenetico import AlgoritmoGenetico
from Cidade import Cidade
# Configuração do algoritmo

tamPopulacao = 100
numGeracoes = 1000
torneio = 5
taxaCruzamento = 0.7
taxaMutacao = 0.4
# Entrada com a quantidade de cidades
qtdCidades = int(input("Digite a quantidade de cidades: "))

cidades = []
# Entre com as cordenadas X e Y das cidades
# X e Y na mesma linha e enter para confirmar a cordenada da cidade
for i in range(qtdCidades):
    x, y = input().split();
    x = int(x);
    y = int(y);
    cidade = Cidade(x, y)
    cidades.append(cidade)


populacao = []
# Gera uma população aletaria por meio de permutação
# A função permutation é da biblioteca np
# Ela gera gera permutações aleatorias entre as cidades
for i in range(tamPopulacao):
    rotas = np.random.permutation(qtdCidades)
    populacao.append(rotas)
    
# Cria uma instancia da classe AlgoritmoGenetico pora realizar as operações
execucaoAlgoritmo = AlgoritmoGenetico(populacao, numGeracoes, torneio, taxaCruzamento, taxaMutacao)

# Loop que será responsável por executar o algoritmo
# Ela primerio calcula a apitidão de cada individuo
# Depois ela pega os selecionados, ou seja os mais aptos
for geracao in range(numGeracoes):
    aptidoes = [execucaoAlgoritmo.realizarAptidao(rotas, cidades) for rotas in populacao]
    selecionados = execucaoAlgoritmo.realizarSelecao(populacao, aptidoes, torneio)
    
    novaPopulacao = []
    
    # Nesse trexo de codigo é feita o cruzamento e a mutação entre os 
    # individuos, depois é verificado se o numero aleatorio sorteado esta abaixo da taxa de cruzamento
    # Se estiver e feito o cruzamento entre os individuos
    # Se não, os proprios pais são adicionados na nova população
    for i in range(0, len(selecionados), 2):
        pai = selecionados[i]
        mae = selecionados[i+1]
        
        if random.random() < taxaCruzamento:
            filho1, filho2 = execucaoAlgoritmo.realizarCruzamento(pai, mae)
            filho1 = execucaoAlgoritmo.realizarMutacao(filho1, taxaMutacao)
            filho2 = execucaoAlgoritmo.realizarMutacao(filho2, taxaMutacao)
            
            novaPopulacao.append(filho1)
            novaPopulacao.append(filho2)
        else:
            novaPopulacao.append(pai)
            novaPopulacao.append(mae)
        
    populacao = novaPopulacao

# Irá printar na tela o melhor caminho encontrado junto com sua distancia
aptidoes = [execucaoAlgoritmo.realizarAptidao(rotas, cidades) for rotas in populacao]
# Função argmin retorna o indice do individuo com o menor aptidão
melhor = np.argmin(aptidoes)
melhorRota = populacao[melhor]
distancia = aptidoes[melhor]

print("Melhor solucao")
print("Rota entre as cidades:", melhorRota)
print("Distancia total:", distancia)