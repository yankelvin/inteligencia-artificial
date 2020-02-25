# Imports necessários
import random
from deap import creator, base, tools, algorithms

# Define o tipo fitness: Um objetivo com maximização
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Define o tipo indivíduo: indivíduo do tipo list (array) com
# a fitness definida anteriormente.
creator.create("Individual", list, fitness=creator.FitnessMax)

# Toolbox para inicialização de componentes do algoritmo
toolbox = base.Toolbox()

# Atributo booleano criado de forma aleatório
toolbox.register("attr_bool",
                 random.randint, 0, 1)

# Indivíduo (tipo Inidividual) criado a partir do atributo definido
# anteriormente. Ou seja, indivíduo do tipo booleano.
# São criados 100 indivíduos. initRepeat faz esse papel
toolbox.register("individual",
                 tools.initRepeat, creator.Individual, toolbox.attr_bool, n=7)

# Criação da população, do tipo lista composto
# por indivíduos (individual)
toolbox.register("population",
                 tools.initRepeat, list, toolbox.individual)

score = [{'value': 6, 'weight': 2},
         {'value': 5, 'weight': 3},
         {'value': 8, 'weight': 6},
         {'value': 9, 'weight': 7},
         {'value': 6, 'weight': 5},
         {'value': 7, 'weight': 9},
         {'value': 3, 'weight': 4},
         ]

# Criação da função de fitness.
# A função recebe um indivíduo e retorna uma tupla
# que representa a avaliação do indivíduo


def evalOneMax(individual):
    value = 0
    weight = 0

    for i in range(len(individual)):
        if individual[i] == 1:
            value += score[i]['value']
            weight += score[i]['weight']

    return {'value': [value], 'weight': weight}


# registra a função de fitness
toolbox.register("evaluate", evalOneMax)

# registro dos operadores
toolbox.register("mate", tools.cxTwoPoint)  # crossover
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)  # mutação

# registro do método de seleção
toolbox.register("select", tools.selTournament, tournsize=3)

# tamanho da população
population = toolbox.population(n=300)


# iniciando o processo de evolução

NGEN = 40  # número de gerações
for gen in range(NGEN):

    # O módulo algorithms implementa vários algoritmos evolucionários
    # Na documentação tem a lista:
    # https://deap.readthedocs.io/en/master/api/algo.html
    # varAnd aplica operações de mutação e crossover
    # cxpb: probabilidade de crossover
    # mutpb: probabilidade de mutação
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    # avalia cada indivíduo
    fits = toolbox.map(toolbox.evaluate, offspring)

    # associa cada indivíduo ao seu valor de fitness
    for fit, ind in zip(fits, offspring):
        if fit['weight'] > 9:
            ind.fitness.values = [0]
        else:
            ind.fitness.values = fit['value']

    # aplica a seleção para gerar a nova população
    population = toolbox.select(offspring, k=len(population))

# retorna o k melhor indivíduos da última população
top10 = tools.selBest(population, k=10)

# Imprime o melhor
print(top10[0])
print(evalOneMax(top10[0]))
