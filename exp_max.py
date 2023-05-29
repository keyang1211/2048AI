"""
Expectimax algorithm for 2048.

"""

from mylogic import *
from copy import deepcopy
import numpy as np
#from heuristic_optimal import * #optimal model
from heuristic_simple import * #basic model

def utility(state):
    l1=[]
    for i in range(len(state[0])):
        l1.append(max(state[i]))
    return max(l1)
def possiblestate(state):
    l1=[]
    for i in range(len(state[0])):
        for j in range(len(state[0])):
            if state[i][j]==0:
               new_2state=deepcopy(state) 
               new_4state=deepcopy(state) 
               new_2state[i][j]=2
               new_4state[i][j]=4
               l1.append(new_2state)
               l1.append(new_4state)
    return l1

#Testing:
# a=[[0,0,0,4],[2,0,0,0],[0,0,0,0],[0,0,0,0]]
# print(possiblestate(a))



def exp_max(state,step=1):
    if step>2: ##the depth = 3
    #if step>4: ##the depth = 5
        list_possiblestate=possiblestate(state)
        list_temp1=[]
        for i in list_possiblestate:
            list_temp1.append(evaluate(i))

        return sum(list_temp1)/len(list_temp1)
    
    if step%2==1:
        list_possiblestate=possiblestate(state)
        list_temp1=[]
        step=step+1
        for i in list_possiblestate:
               # check state
            if check_state(i)=='win':
                list_temp1.append(evaluate(i))
            elif check_state(i)=='lose':
                list_temp1.append(evaluate(i))
            else:
                list_temp1.append(exp_max(i,step))
        return sum(list_temp1)/len(list_temp1)
    
    if step%2==0:
        step=step+1
        l1=[]
        if up(state)!=state:
            l1.append(exp_max(up(state), step))
            
        if down(state)!=state:
            l1.append(exp_max(down(state), step))    
        
        if left(state)!=state:
            l1.append(exp_max(left(state), step))

        if right(state)!=state:
            l1.append(exp_max(right(state), step))
            
        return max(l1)
 
            
#For testing:
         
# c=[[0,0,0,4],[0,0,16,8],[0,128,256,256],[0,256,512,1024]]

# a=exp_max(up(c))
# b=exp_max(down(c))
# d=exp_max(left(c))
# e=exp_max(right(c))
# print(a,b,d,e)
# c=[[4,2,4,4],[2,8,64,8],[8,32,128,32],[1024,512,256,64]]
# c=left(c)
# print_game(c)
