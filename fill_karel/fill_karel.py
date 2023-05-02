from stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def go_back():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()
    
    
def change_avenue():
    turn_left()
    move()
    turn_right()
    
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def fill_street():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
 

def main():
    while front_is_clear():
        if left_is_clear():
            fill_street()
            go_back()
            change_avenue()
        else:
            fill_street()


# There is no need to edit code beyond this point
if __name__ == '__main__':
   run_karel_program()