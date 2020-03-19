# logistic regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("reading data")
# edit the path for your data.csv file should be entered below
inde_data = pd.read_csv("C:/Users/Apratim Ray/Desktop/DESKTOP/Hashing/assingment/ML/data.csv",usecols=["x"]).to_numpy()
dep_data = pd.read_csv("C:/Users/Apratim Ray/Desktop/DESKTOP/Hashing/assingment/ML/data.csv",usecols=["y"]).to_numpy()


inde_data = np.reshape(inde_data,(len(inde_data)))
dep_data = np.reshape(dep_data,(len(dep_data)))
print("reading data done")


# the logistic function
"""
when fitting 
please subtract the input with pos variable
instead of adding

P.S. never mind just insert it in negetive form don in line 37
"""
def logistic(parameter1):
    return (1/(1+np.exp(-parameter1)))

# initial starting position
pos = 1

# matplotlib stuff
x = np.array(range(30))


def total_cost_calc(inde_data,dep_data,pos):
    total_cost = 0
    for temp1 in range(len(inde_data)):
        #subtracted and entered into the log function here------↓
        total_cost += (dep_data[temp1]-logistic(inde_data[temp1]-pos))**2
    return total_cost

def pos_adjuster(inde_data,dep_data,pos,step_size):
    temp1 = total_cost_calc(inde_data,dep_data,pos-step_size)
    temp2 = total_cost_calc(inde_data,dep_data,pos+step_size)

    comp_array = [temp1, temp2]

    min_pos = comp_array.index(min(comp_array))

    if min_pos == 0:
        pos -= step_size
    else:
        pos += step_size

    return pos

step_size = 1
step_size_decider_constant = 0
pos_nochange_array = [0]*3

def step_size_decider(parameter1):
    global step_size
    global step_size_decider_constant
    global pos_nochange_array

    step_size_decider_constant = (step_size_decider_constant + 1) % 3
    pos_nochange_array[step_size_decider_constant] = parameter1

    if pos_nochange_array[0]==pos_nochange_array[2]:
        step_size = step_size*0.5



for temp1 in range(1000):
    pos = pos_adjuster(inde_data,dep_data,pos,step_size)
    print(pos,step_size)
    y = logistic(x-pos)
    plt.plot(x,y)
    step_size_decider(pos)

print("threshold is at ",pos,"and step size is = ",step_size)
plt.plot(inde_data,dep_data,"ro")
plt.show()