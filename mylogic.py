""""
Logic to build 2048 game. 

Initilize new game, functions to slide and merge tiles in game.

"""

import random
import numpy as np
from copy import deepcopy

#Build a 4*4 matrix, two of the bricks are randomly 2 or 4 
#and rest of others are 0.
def init_game(matrix):
    x1  = random.randint(0, len(matrix)-1)
    y1  = random.randint(0, len(matrix)-1)
    x2  = random.randint(0, len(matrix)-1)
    y2  = random.randint(0, len(matrix)-1)
    if matrix[x1][y1] == 0 | matrix[x2][y2] == 0 |y1 != y2:
        matrix[x1][y1] = random.randrange(2,5,2)
        matrix[x2][y2] = random.randrange(2,5,2)
    else:
        init_game(matrix)
    return matrix

def new_game(n):
    matrix = [[0 for i in range(n)] for i in range(n)]
    matrix = init_game(matrix)
    
    return matrix



#Set a function to check the game is win/lose/continue.
def check_state(state):
    #if the max value is more than 2048, then win.
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] >= 9999999:
                return 'win'
            
    #if there still has blank or there has bricks could be merged,
    #then continue.
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return 'continue' 
    for i in range(len(state)-1):
        for j in range(len(state[0])-1):
            if state[i][j] == state[i+1][j] or state[i][j] == state[i][j+1]:
                return 'continue'
    for i in range(len(state)-1):
        if state[i][len(state[0])-1] == state[i+1][len(state[0])-1]:
            return 'continue'
    for j in range(len(state[0])-1):
        if state[len(state)-1][j] == state[len(state)-1][j+1]:
            return 'continue'   
    
    #if there's no blank and could not move, then lose.
    return 'lose'


#moving part:

def transpose(state):
    tmp = list(map(list,zip(*state)))
    return tmp

def reverse(state):
    n = 4
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in range(len(state)):
        for j in range((len(state[0])//2)):
            matrix[i][j] = state[i][(len(state[0])-1-j)]
            matrix[i][(len(state[0])-1-j)] = state[i][j]
    return matrix      

            
#implement a function to do the compress active
#the compress direction is left(as player press <-)
def compress(state): 
    #make a empty matrix to save result
    n = len(state[0]) #set the same size of the game
    result = [[0 for i in range(n)] for i in range(n)]
    
    #traverse all cells to find out empty block and shift number to the place
    for i in range(len(state)):
        pjt = 0 #set a value as coordinate to project num to result matrix
        for j in range(len(state[0])):
            if state[i][j] != 0:
                result[i][pjt] = state[i][j]
                pjt = pjt+1
    return result
    

#let's implement a function to merge to left side, the merge will be located on rows.
def merge(state):
    result=deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[0])-1):
            if(state[i][j] == state[i][j+1] & state[i][j] != 0):
                result[i][j] = state[i][j] * 2
                result[i][j+1] = 0
    return result

#implement a function that every move will add a new brick

def add_brick(state):
    x  = random.randint(0, len(state)-1)
    y  = random.randint(0, len(state)-1)

    if state[x][y] == 0:
        state[x][y] = random.randrange(2,5,2)
    else:
        add_brick(state)
    return state

#define the function of 4 direction movement.
#left --> compress -> merge -> compress
def left(state):
    state = compress(merge(compress(state)))
    return state

#right --> reverse -> left -> reverse
def right(state):
    state = reverse(left(reverse(state)))
    return state

#up --> transpose -> left -> transpose
def up(state):
    state = transpose(left(transpose(state)))
    return state

#down --> transpose -> reverse -> left -> reverse -> transpose
def down(state):
    state = transpose(reverse(left(reverse(transpose(state)))))
    return state

def print_game(state):
    temp=deepcopy(state)
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            if temp[i][j]==0:
                temp[i][j]='.'
            print('%s\t'%temp[i][j],end='')
        print('')

       
            

############ test ##########
'''
a = new_game(4) #test
#print(a)
#tmp = list(map(list,zip(*a)))
#tmp1 = a[::-1]

#result = compress(a) 

transpose_t = transpose(a)
reverse_t = reverse(a)
left_t = left(a)
right_t = right(a)
up_t = up(a)
down_t = down(a)




print_game(a)
'''















