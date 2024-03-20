import numpy as np
import statistics
import random
import matplotlib.pyplot as plt


#simulates a game
def game(glasses, glasses_no):
    
    new_amounts = [0.0] * glasses_no
    choice = 0


    for i in range(1000):
        #Ali's turn

        for j in range(glasses_no):
            new_amounts[j] = random.random() 

        total = 2*sum(new_amounts)
        for j in range(glasses_no):
            new_amounts[j] = new_amounts[j] / total
            glasses[j] = glasses[j] + new_amounts[j]




        #test if glass overflows 
        for j in glasses:
            if j > 1:
                return("Ali")
                

        #Beth's turn
        choice = random.randint(0, glasses_no-1)
        glasses[choice] = 0.0
        glasses[(choice+1) % glasses_no] = 0.0

    return("Beth")




#simulates many games and creates a histogram of the results
iterations = 1000
Ali_win_rate = [0.5] * 5

for n in range(3, 8):
    results = [0.0] * iterations
    for i in range(iterations):
        glasses = [0] * n
        outcome = game(glasses, n)
        if outcome == "Ali":
            results [i] = 1.0
    Ali_win_rate[n-3] = statistics.mean(results)
    print(n, ":, ", Ali_win_rate)


'''
xpoints = range(3, 8)

plt.plot(xpoints, Ali_win_rate)
plt.xlabel("Number of glasses")
plt.ylabel("Ali's winrate")
plt.ylim(-0.2, 1.2)


plt.show()
    
print(Ali_win_rate[0])

'''