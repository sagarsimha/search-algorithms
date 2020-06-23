import random
import copy
import numpy as np

def IntermediateLineRecombination(solution_a, solution_b):
    prob = 0.25
    sol_a_copy = copy.deepcopy(solution_a)
    sol_b_copy = copy.deepcopy(solution_b)
    sol_length = len(sol_a_copy)

    for i in range(sol_length):
        while True:
            alpha = random.uniform(-prob, 1 + prob)
            beta = random.uniform(-prob, 1 + prob)
            t = (alpha * sol_a_copy[i]) + ((1 - alpha) * sol_b_copy[i])
            s = (beta * sol_b_copy[i]) + ((1 - beta) * sol_a_copy[i])
            if bound(solution_a, solution_b, t, s):
                break
        sol_a_copy[i] = t
        sol_b_copy[i] = s

    return sol_a_copy, sol_b_copy


def bound(sol_a_copy, sol_b_copy, t, s):
    maxA = max(sol_a_copy)
    minA = min(sol_a_copy)
    maxB = max(sol_b_copy)
    minB = min(sol_b_copy)
    if (minA - 1) <= t <= (maxA + 1) and (minB - 1) <= s <= (maxB + 1):
        return True
    return False

print(IntermediateLineRecombination([1,1,1],[1.23,1.4,2]))