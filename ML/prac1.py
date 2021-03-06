import numpy as np
import matplotlib.pyplot as plt
import random as rn

train_data_independent= np.array([3,4,6,7,12,14,17,15,7,9,11,14,20],np.uint8)

train_data_dependent= np.array([2,3,5,8,11,14,17,15,7,9,11,14,20],np.uint8)


slope = rn.randint(-1000,1000)  #these are random initial position
constant = rn.randint(-1000,1000) 
total_cost = 0
step_size_decider_constant = 0

n_slope_p = [0,0,0]
n_constant_p = [0,0,0]

#step size can be turned small but will increase the number of itterations
step_size = 10

#matplotlib stuff
x = np.array(range(30))



def cost_calculate(array_pos,n_slope,n_constant):
	temp_cost = (n_slope*train_data_independent[array_pos] + n_constant)-train_data_dependent[array_pos]
	temp_cost = temp_cost*temp_cost
	return temp_cost


def actual_total_cost(n_slope,n_constant):
	global total_cost
	total_cost = 0
	# dont know why for loop goes out of array index when not specified 
	for temp1 in range(13):
		temp3 = cost_calculate(temp1,n_slope,n_constant)
		
		total_cost = total_cost + temp3
	return total_cost

def decider(n_slope,n_constant):


	temp1 = actual_total_cost(n_slope,n_constant)
	temp2 = actual_total_cost(n_slope+step_size,n_constant)
	temp3 = actual_total_cost(n_slope,n_constant+step_size)
	temp4 = actual_total_cost(n_slope-step_size,n_constant)
	temp5 = actual_total_cost(n_slope,n_constant-step_size)
	temp6 = actual_total_cost(n_slope+step_size,n_constant+step_size)
	temp7 = actual_total_cost(n_slope-step_size,n_constant-step_size)
	temp8 = actual_total_cost(n_slope+step_size,n_constant-step_size)
	temp9 = actual_total_cost(n_slope-step_size,n_constant+step_size)

	#these are the weights
	print(temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9)

	comp_array = [temp1,temp2,temp3,temp4,temp5,temp6,temp7,temp8,temp9]

	minpos = comp_array.index(min(comp_array))

	if minpos == 1 :
		n_slope = n_slope+step_size

	elif minpos == 2:
		n_constant = n_constant +step_size

	elif minpos == 3:
		n_slope = n_slope-step_size

	elif minpos == 4:
		n_constant = n_constant-step_size

	elif minpos == 5:
		n_constant = n_constant + step_size
		n_slope = n_slope + step_size

	elif minpos == 6:
		n_constant = n_constant - step_size
		n_slope = n_slope - step_size


	elif minpos == 7:
		n_slope = n_slope + step_size
		n_constant = n_constant - step_size

	elif minpos == 8:
		n_slope = n_slope - step_size
		n_constant = n_constant + step_size
	
	elif minpos == 0:
		n_slope = n_slope
		n_constant= n_constant


	# else :
	# 	n_slope = n_slope
	# 	n_constant = n_constant
	#print(n_slope,n_constant)
	return n_slope,n_constant

def step_size_decider(n_slope,n_constant):
	global step_size_decider_constant
	global step_size
	step_size_decider_constant = (step_size_decider_constant + 1)%3
	n_slope_p[step_size_decider_constant] = n_slope
	n_constant_p[step_size_decider_constant] = n_constant

	if (n_constant_p[0] == n_constant_p[1] == n_constant_p[2]) and (n_slope_p[0] == n_slope_p[1] == n_slope_p[2]) :
		step_size = step_size * 0.5
	else :
		step_size = step_size


for temp3 in range(1000):
	slope,constant = decider(slope,constant)
	y = x*slope + constant
	plt.plot(x,y)
	step_size_decider(slope,constant)
	print("step size is ",step_size)




print(slope,constant)

#initial plot of points
plt.plot(train_data_dependent,train_data_independent,'ro')

plt.show()