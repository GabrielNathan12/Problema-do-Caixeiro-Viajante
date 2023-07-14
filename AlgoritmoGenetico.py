import math
import random
import numpy as np

# Classe resposavel pela execução do algoritmo genetico
class AlgoritmoGenetico:
    # Construtor da classe
    # Recebe como parametro a  lista de população
    # o numero de geracoes 
    # o tamanho do torneio
    # a taxa de cruzamento 
    # e a taxa de mutacao das geracoes
    def __init__(self, populacao, geracoes, torneio, cruzamento, mutacao):
        self.populacao = populacao
        self.geracoes = geracoes
        self.torneio = torneio
        self.cruzamento = cruzamento
        self.mutacao = mutacao
    
    # Funcao que calcula a distancia total entre 2 cidades
    # Usando a formula de calcular pontos
    def distanciaTotal(self, cidadeOri, cidadeDest):
        distancia = math.sqrt(((cidadeDest.getX() - cidadeOri.getX())**2) + ((cidadeDest.getY() - cidadeOri.getY())**2))
        return distancia
    
    # Funcao que calcula a aptidao de uma rota
    # Funcao recebe como parametro as rotas e as cidades
    # e vai somando a distancia entre as cidades, tambem considera,
    # a ultima cidade visitada e a cidade de origem para fazer a soma de todos 
    def realizarAptidao(self, rota, cidades):
        distanciaTotal = 0
        numCidades = len(rota)
        
        for i in range(numCidades - 1):
            cidadeAtual = cidades[rota[i]]
            proximaCidade = cidades[rota[i+1]]
            distanciaTotal += self.distanciaTotal(cidadeAtual, proximaCidade)
            
        ultimaVisitada = cidades[rota[numCidades - 1]]
        cidadeOrigem = cidades[rota[0]]
        distanciaTotal += self.distanciaTotal(ultimaVisitada, cidadeOrigem)
        
        return distanciaTotal
    
    # Funcao responsavel por fazer a selecao dos mais aptos
    # Essa funcao recebe como parametro 
    # a população, a lista de aptidões e o tamanho do torneio
    # A função itera sobre a população e seleciona aleatoriamente um
    # subconjunto de indivíduos com base no tamanho do torneio
    # Em seguida, escolhe o indivíduo mais apto desse subconjunto como vencedor do torneio
    # A função se repete até selecionar todos os indivíduos da próxima geração
    def realizarSelecao(self, populacao, aptidao, tamTorneio):
        selecionar = []
        
        for i in range(len(populacao)):
            competidores = random.sample(range(len(populacao)), tamTorneio)
            vencedor = min(competidores, key=lambda x:aptidao[x])
            selecionar.append(populacao[vencedor])            
        return selecionar
    # Funcao responsavel por fazer o cruzamento entre as rotas
    # Ela recebe duas rotas como parâmetros
    # A função escolhe aleatoriamente um ponto de corte
    # e divide as rotas em duas partes
    # Os segmentos de uma rota são combinados com os elementos não presentes
    # na outra rota para formar as rotas descendentes
    def realizarCruzamento(self, rota, rota2):
        corte = random.randint(0, len(rota) -1)
        filho1 = np.concatenate((rota[:corte], [x for x in rota2 if x not in rota[:corte]]))
        filho2 = np.concatenate((rota2[:corte], [x for x in rota if x not in rota2[:corte]]))
        
        return filho1, filho2
    
    # Função responsável por fazer a mutação das rotas
    # Ela recebe a rota e a taxa de mutação como parâmetros
    # Com uma probabilidade igual à taxa de mutação, a função seleciona
    # aleatoriamente dois índices na rota e troca as cidades correspondentes
    def realizarMutacao(self, rota, mutacao):
        if random.random() < mutacao:
           index = random.sample(range(len(rota)), 2)
           rota[index[0]], rota[index[1]] = rota[index[1]], rota[index[0]]
        
        return rota