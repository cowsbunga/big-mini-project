import numpy as np
import math


#simulates a game
def game(glasses, glasses_no):
    
    amount = 0.5/glasses_no
    choice = 0


    for i in range(1000):
        #Ali's turn
        for j in range(glasses_no):
            glasses[j] = glasses[j] + amount


        #test if glass overflows 
        for j in glasses:
            if j > 1:
                return("Ali")
                

        #Beth's turn
        choice = (choice + 2) % glasses_no
        glasses[choice] = 0.0
        glasses[(choice+1) % glasses_no] = 0.0

    
    return("Beth")


glasses_no = int(input("number of glasses: "))
glasses = [0.0] * glasses_no
winner = game(glasses, glasses_no)
print("winner is ", winner)
