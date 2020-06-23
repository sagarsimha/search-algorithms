# Stochastic Universal Sampling takes in n individuals of a generation and 
# samples n individuals towards next generation
import math
import random
from copy import deepcopy
import copy
import numpy as np

def Stochastic_Universal_Sampling(pop, features, interactions):
    n = len(pop)
    pop_s = deepcopy(pop)
    
    #Random shuffle the population
    random.shuffle(pop_s)
    
    # f is the fitness array built using the fitness assesment function
    f = []
    for ps in pop_s:
        f.append( assessfitness(ps, features, interactions) )
    
    #Scaling all fitnesses onto positive axis by adding the minimum value to avoid negative fitnesses.
    #This step only scales the fitnesses up or down the positive axis and doesn't alter 
    #the relationship between them. This part is only required for Task 4
    scale_positive = min(f)
    for i in range(len(f)):
        f[i] += scale_positive*-1

    index = 0
    
    # In case all fitnesses are zero, changing to 1 to allow a small chance of being selected
    zeros = all(x==0 for x in f)
    if(zeros):
        for i in range(len(f)):
            f[i] = 1
    
    # Cumulative Distribution Function
    cdf = f 
    for i in range(1, len(f)):
        cdf[i] = cdf[i-1]+cdf[i]
    
    #The cumulative sum of fitnesses (The last element in cdf)
    fl = cdf[-1] 
    
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