import numpy as np
import statistics
import random
import matplotlib.pyplot as plt


#simulates a game
def game(glasses, glasses_no):
    new_amounts = [0.0] * glasses_no

    for i in range(1000):

        #Ali's turn
        for j in range(glasses_no):
            new_amounts[j] = random.random() 

        total = 2*sum(new_amounts)
        for j in range(glasses_no):
            new_amounts[j] = new_amounts[j] / total
            glasses[j] = glasses[j] + new_amounts[j]
        
        

        #test if a glass overflows
        for j in range(glasses_no):
            if glasses[j] > 1:
                return("Ali")


        #Beth's turn
        j_max = 0
        for j in range(glasses_no):
            if glasses[j] >= j_max:
                j_max = glasses[j]
                index = j
        
        glasses[index] = 0.0
        if glasses[(index+1) % glasses_no] > glasses[(index-1) % glasses_no]:
            glasses[(index+1) % glasses_no] = 0.0
        else:
            glasses[(index-1) % glasses_no] = 0.0  


    return("Beth")

trials = 100000
beth_wins = 0

for i in range(trials):
    glasses = [0.0] * 5
    result = game(glasses, 5)
    if result == "Beth":
        beth_wins += 1

print(beth_wins)
