import numpy as np
import statistics
import random
import matplotlib.pyplot as plt


#simulates a game
def game(glasses, glasses_no):
    

    for i in range(1000):
        #Ali's turn
        glasses[0] += 0.25
        glasses[2] += 0.25
        
        #if i < 30:
        #    print("Ali: ", glasses)


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

        #if i < 30:
        #    print("Beth: ", glasses)


        #test if Ali has winning condition
        for j in range(glasses_no-1):
            for k in range(j+1, glasses_no):
                if glasses[j] + glasses[k] > 0.5: 
                    return("Ali")
        
        


    return("Beth")



glasses = [0.0] * 5
result = game(glasses, 5)
print(result)
