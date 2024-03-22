import numpy as np
import statistics
import random
import matplotlib.pyplot as plt


#simulates a game
def game(glasses, glasses_no):
    

    for i in range(1000):

        #Ali's turn
        method_one = False
        method_two = False
        for j in range(glasses_no):
            if glasses[j] > 0.5:
                method_one = True
                j_imp = j
            for k in range(j):
                if glasses[j] + glasses[k] > 0.5:
                    method_two = True
                    j_imp_one = k
                    j_imp_two = j


        if method_one == True:
            glasses[j_imp] += 0.5 
        
        elif method_two == True:
            glasses[j_imp_one] += 0.25
            glasses[j_imp_two] += 0.25

        elif glasses[0] > 0.24 or glasses[1] > 0.24 or glasses[2] > 0.24:
            empty_added = False
            full_added = False
            for j in range(glasses_no):
                if glasses[j] == 0.0 and empty_added == False:
                    glasses[j] = 0.26
                    empty_added = True
                elif glasses[j] > 0.24:
                    if full_added == False:
                        glasses[j] += 0.02
                        full_added = True
                    else:
                        glasses[j] += 0.11

        else:
            diff = 0
            for j in range(glasses_no):
                if glasses[j] > 0:
                    diff = glasses[j]
            additional = (0.5 - diff - diff) / 5

            for j in range(glasses_no):
                if glasses[j] == 0:
                    glasses[j] = diff + additional
                else:
                    glasses[j] += additional

        
        if i < 10:
            print("Ali: ", glasses)

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


        if i < 10:
            print("Beth: ", glasses)

        


    return("Beth")



glasses = [0.0] * 5
result = game(glasses, 5)
print(result)
