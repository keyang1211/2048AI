# -*- coding: utf-8 -*-
"""

@author: HP
"""

from mylogic import transpose, reverse, check_state
Weight_matrix = [[16,   9,  8,  1],    
           [15,  10,  7,  2],   
           [14,  11,  6,  3],    
           [13,  12,  5,  4]]   


def optimal_model(m1 = Weight_matrix):
    m2 = reverse(m1)
    m3 = transpose(m2)
    m4 = reverse(m3)

    return [m1, m2, m3, m4]


optimal = optimal_model()


def _utility_func(state):
    sums = [0] * 8 
    for i in range(len(state)):
        for j in range(len(state[0])):
            for k in range(4):
                sums[k] += optimal[k][i][j] * state[i][j]
                
    return max(sums)

def evaluate(state):
    if check_state(state) == 'lose':
        return 0
    score = _utility_func(state)
    if check_state(state) == 'win':
        return 0
    else:
        return score



