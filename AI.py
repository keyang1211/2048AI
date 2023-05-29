"""
Run file to initialize AI playing 2048.

Finial AI for playing 2048 using expectimax algorithm and heuristics.

"""

from mylogic import *
from copy import deepcopy
import numpy as np
from exp_max import *


if __name__ == "__main__":
    i = 0
    result = np.zeros(15)
    for i in range(0,15):            
        dic_move={0:up,1:down,2:left,3:right}
        game=new_game(4)
        step=1
        while True:
            state=check_state(game)
            if state=='win':
                print_game(game)
                print('#############')
                print('it is the', step, 'step')
                break
            elif state=='continue':
                print_game(game)
                print('#############')
                print('it is the', step, 'step')
            elif state=='lose':
                print_game(game)
                print('#############')
                print('it is the', step, 'step')
                print('you lose')
                break
            l1=[]
            if up(game)!=game:
                l1.append(exp_max(up(game)))  
            else:
                l1.append(0)
                
            if down(game)!=game:
                l1.append(exp_max(down(game)))
            else:
                l1.append(0)
            if left(game)!=game:
                l1.append(exp_max(left(game)))
            else:
                l1.append(0)
            if right(game)!=game:
                l1.append(exp_max(right(game)))
            else:
                l1.append(0)   
            a=l1.index(max(l1))
            game=dic_move[a](game)
            add_brick(game)
            
            maxi = np.max(game)
            step = step + 1

        result[i] = maxi
        i = i + 1