# -*- coding: utf-8 -*-
"""

@author: HP
"""

from mylogic import transpose, reverse, check_state

#the s-shape WM
Weight_matrix = [[16,   9,  8,  1],    
           [15,  10,  7,  2],   
           [14,  11,  6,  3],    
           [13,  12,  5,  4]]   

'''
Weight_matrix = [[61,  33,  29,  1],    
           [57,  37,  25,  5],   
           [53,  41,  21,  9],    
           [49,  45,  17,  13]]   

##the radiation like WM
Weight_matrix = [[16,  12,  8,  6],    
           [12,  10,  8,  4],   
           [8,  8,  6,  4],    
           [6,  4,  4,  2]]   
'''
#function to sum the score
def _utility_func(state):
    sum0 = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            sum0 += Weight_matrix[i][j] * state[i][j]
    return sum0

def evaluate(state):
    if check_state(state) == 'lose':
        return 0

    score = _utility_func(state)
    if check_state(state) == 'win':
        return 0
    else:
        return score