"""
Run file to manually play 2048 game. 

Initialize and run game, using input from user.

"""
import os
a=os.path.split(__file__)[0]
import sys
sys.path.append(a)
from mylogic import *
from copy import deepcopy
if __name__ == "__main__":
    
    print("Size of board")
    size = int(input("Size: "))
    print("Creating game...")
    game=new_game(size)
    invalid_move=0

    while True:
        if invalid_move==1:
            print('invalid move')
            print_game(game)
            invalid_move=0
        elif invalid_move==0:
            state=check_state(game)
            if state=='win':
                print_game(game)
                print('you win')
                break
            elif state=='continue':
                print_game(game)
            elif state=='lose':
                print_game(game)
                print('you lose')
                break
        
        previous_game=deepcopy(game)
        print('w=↑, a=←, s=↓, d=→,To quit, enter "q"')
        m=input('Move')
        if m=='w':
            game=up(game)
            if game!=previous_game:
               add_brick(game)
        elif m=='a':
            game=left(game)
            if game!=previous_game:
               add_brick(game)
        elif m=='s':
            game=down(game)
            if game!=previous_game:
               add_brick(game)
        elif m=='d':
            game=right(game) 
            if game!=previous_game:
               add_brick(game)
        elif m=='q':
            break
        else:
            invalid_move=1
         