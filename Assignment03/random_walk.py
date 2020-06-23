import random
import numpy as np

def random_walk(pop,low,high):
	p = 1/len(pop)
	b = 0.7


	for x in range(len(pop)):
		if p >= random.random():
			while(1):
				n = random.choice([1,-1])
				if low_bound <= pop[x]+n <= high_bound:
					pop[x]+=n
				elif low_bound <= pop[x]-n <= high_bound:
					pop[x]-=n 

				if b< random.random():
					break

	return pop


low_bound = 1
high_bound = 100
pop = np.random.randint(low_bound, high_bound+1, size=20)
print('Initial Population',pop)
mutated_pop=random_walk(pop,low_bound,high_bound)
print('Mutatted Population',mutated_pop)