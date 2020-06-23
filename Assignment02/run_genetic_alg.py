#!python3
import sys
import math
import random
from copy import deepcopy
import copy
import numpy as np


def main(features, interactions):
	max_evals = 100
	evals = 0
	feature_size = len(features)
	pop_size = 16 #Even number
	crossover = uniform_crossover# uniform_crossover #one_point_crossover, #two_point_crossover

	P = initialize_population(feature_size, pop_size)
	P0 = P[0]
	Best = P0
	# print(Best)

	while(evals<=max_evals):
	    evals +=1
	    for p in P:
	        if (Best==P0 or (assess_fitness(p,features,interactions)>assess_fitness(Best,features,interactions))):
	            Best = p
	    Q=[]
	    P_new = Stochastic_Universal_Sampling(P, features, interactions)
	    for i in range(0,pop_size,2):
	        Pa = P_new[i]
	        Pb = P_new[i+1]
	        Ca, Cb = crossover(copyS(Pa),copyS(Pb))
	        Q.extend([tweak(Ca), tweak(Cb)])
	    P = Q
	print("The Optimal Configuration found: ", Best)
	print("The Performance is: ", assess_fitness(Best, features, interactions))

# def optimize(population):
#     # TODO: to implement
#     pass


def initialize_population(feature_size, pop_size):
    init_population = []
    for _ in range(pop_size):
        par = []
        for _ in range(feature_size):
            par.append(random.choice([0, 1]))
        init_population.append(par)

    return init_population


def copyS(solution):
    return copy.deepcopy(solution)


def tweak(solution):
    prob = 1 / len(solution)
    sol = copy.deepcopy(solution)

    for i in range(len(sol)):
        if prob >= random.random():
            sol[i] ^= 1
    return sol

def choose_random(sol_length):
    return np.random.randint(0, sol_length)

#Select operation
# Stochastic Universal Sampling takes in n individuals of a generation and samples n individuals towards next generation
def Stochastic_Universal_Sampling(pop, features, interactions):
    n = len(pop)
    pop_s = deepcopy(pop)
    random.shuffle(pop_s)
        
    f = []
    for ps in pop_s:
        f.append( assess_fitness(ps, features, interactions) )
    
    #Scaling all fitnesses onto positive axis by adding the minimum value to avoid negative fitnesses.
    #This step only scales the fitnesses up or down the positive axis and doesn't alter the relationship between them.
    scale_positive = min(f)
    for i in range(len(f)):
        f[i] += scale_positive*-1
    
    index = 0
    
    zeros = all(x==0 for x in f)
    if(zeros):
        for i in range(len(f)):
            f[i] = 1
    
     # Cumulative Distribution Function
    cdf = f 
    for i in range(1, len(f)):
        cdf[i] = cdf[i-1]+cdf[i]
    
    fl = cdf[-1] #The sum of fitnesses-The last element in cdf
    
    scale = fl//n
    value = random.randint(0,scale)
    
    #Next Generation
    picked_pop=[]
    
    #Picking n individuals of the next generation
    for i in range(n):
        while(cdf[index] < value):
            index +=1
        value = value+scale
        picked_pop.append(pop_s[index])

    return picked_pop

def one_point_crossover(solution_a, solution_b):
    sol_a_copy = copy.deepcopy(solution_a)
    sol_b_copy = copy.deepcopy(solution_b)

    sol_length = len(sol_a_copy)

    c = choose_random(sol_length)
    while True:
        if(c != 0):
            break
        c = choose_random(sol_length)
#     print(c)

    for i in range(0, c): #c, sol_length - In textbook
        sol_a_copy[i], sol_b_copy[i] = sol_b_copy[i], sol_a_copy[i]

    return sol_a_copy, sol_b_copy


def two_point_crossover(solution_a, solution_b):
    sol_a_copy = copy.deepcopy(solution_a)
    sol_b_copy = copy.deepcopy(solution_b)

    sol_length = len(sol_a_copy)

    c = choose_random(sol_length)
    d = choose_random(sol_length)
    while True:
        if(c != d):
            if(c > d):
                c, d = d, c
            break
        c = choose_random(sol_length)
        d = choose_random(sol_length)
#     print(c, d)

    for i in range(c, d):
        sol_a_copy[i], sol_b_copy[i] = sol_b_copy[i], sol_a_copy[i]

    return sol_a_copy, sol_b_copy


def uniform_crossover(solution_a, solution_b):
    sol_a_copy = copy.deepcopy(solution_a)
    sol_b_copy = copy.deepcopy(solution_b)

    sol_length = len(sol_a_copy)

    prob = 1 / sol_length

    for i in range(sol_length):
        if prob >= random.random():
            sol_a_copy[i], sol_b_copy[i] = sol_b_copy[i], sol_a_copy[i]

    return sol_a_copy, sol_b_copy


# The fitness function accounts for both features and interactions
def assess_fitness(solution,features,interactions):
    
    featurelist = list(features.keys())
    fitness_val = 0
    for index, val in enumerate(solution):
        fitness_val += (val * features[featurelist[index]])

    for i in range(len(interactions)):
        int_feat_list = interactions[i][0]
        interaction_present = False
        for j in range(len(int_feat_list)):
            if solution[featurelist.index(int_feat_list[j])] == 1:
                interaction_present = True
            else:
                interaction_present = False
                break

        if interaction_present:
            fitness_val += interactions[i][1]
    return fitness_val

def read_lines(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return lines

def get_features(path):
    lines = read_lines(path)
    features = {}
    for line in lines:
        if len(line) <= 0:
            continue
        key = line.split(" ")[0][:-1]
        value = float(line.split(" ")[1])
        features[key] = value
    return features

def get_interactions(path):
    interactions = []
    lines = read_lines(path)
    for line in lines:
        if len(line) <= 0:
            continue
        interaction_key = line.split(" ")[0][:-1].split("#")
        value = float(line.split(" ")[1])
        interactions.append([interaction_key, value])
    return interactions

if __name__ == "__main__":
    # input scheme: run_genetic_alg.py model_features.txt model_interactions.txt
    if len(sys.argv) != 3:
        print("Not a valid input! Please use:" + \
        "python3 run_genetic_alg.py model_features.txt model_interactions.txt")
        sys.exit(0)
    features = get_features(sys.argv[1])
    interactions = get_interactions(sys.argv[2])
    main(features, interactions)
