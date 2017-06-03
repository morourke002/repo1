# 2017-05-21

# gradient descent finds optimal weights (a,b) that reduces prediction error

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

housing_data = pd.DataFrame({'SIZES' : [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700],
							 'PRICE' : [245000,312000,279000,308000,199000,219000,405000,324000,319000,255000]})

print('\nIndexed Original Data Set\n')
print(housing_data)

z = np.polyfit(housing_data.SIZES, housing_data.PRICE,1)
p = np.poly1d(z)
plt.plot(housing_data.SIZES,p(housing_data.SIZES),"+")
plt.show(block=True)

stdized_housing_data = housing_data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

print('\nObjective: Minimize Total SSE of function PREDICT_PRICE = a + b * SIZE\n')

# Step 1: Initialize the weights(a & b) with random values and calculate Error (SSE)
# ask for input
#a = float(input("Enter a value for weight a:\n"))
a = 0.45
#b = float(input("Enter a value for weight b:\n"))
b = 0.75

#predicted price Ypred = a+bX
def predict_price(X):
	return a + b * X

stdized_housing_data['PREDICT_PRICE'] = stdized_housing_data.apply(lambda x: predict_price(x['SIZES']), axis = 1)

# Sum of Squared Errors (SSE) = 1/2 Sum(Actual House Price - Predicted House Price)^2
# = 1/2 Sum(Y-Ypred)^2

def sse(Y,Ypred):
	return np.multiply(0.5,np.square(Y - Ypred))

stdized_housing_data['SSE'] = stdized_housing_data.apply(lambda x: sse(x['PRICE'],x['PREDICT_PRICE']), axis = 1)

# Step 2: Calculate the gradient i.e. change in SSE when the weights (a & b) are changed by a very small value from their original randomly initialized value. This helps us move the values of a & b in the direction in which SSE is minimized.
# partial derivative of SSE with respect to a = -(Y-Ypred)
# partial derivative of SSE with respect to b = -(Y-Ypred)*X
# (SSE = 1/2 * (Y-Ypred)^2 = 1/2 * (Y - (a+b*X))^2)

stdized_housing_data['dSSE/da'] = - (stdized_housing_data.PRICE - stdized_housing_data.PREDICT_PRICE)

stdized_housing_data['dSSE/db'] = -(stdized_housing_data.PRICE - stdized_housing_data.PREDICT_PRICE) * stdized_housing_data.SIZES

print('\nData Set Standardization with Error Gradient\n')
print(stdized_housing_data.sort_values('SIZES'))

totals = stdized_housing_data.sum()

totals_i_want = {'TOTAL_SSE' : totals.loc['SSE'],
				 'TOTAL_dSSE/da' : totals.loc['dSSE/da'],
				 'TOTAL_dSSE/db' : totals.loc['dSSE/db']}

print('\n')
print(totals_i_want)

# Step 3: Adjust the weights with the gradients to reach the optimal values where SSE is minimized
# new rules: a-total_dSSE/da
#			: b-total_dSSE/db

# learning rate
r = 0.01

a = a - r * totals.loc['dSSE/da']
b = b - r * totals.loc['dSSE/db'] 

print('\nNew a\n')
print(a)
print('\nNew b\n')
print(b)

# Step 4: Use the new weights for prediction and to calculate the new SSE

stdized_housing_data['PREDICT_PRICE'] = stdized_housing_data.apply(lambda x: predict_price(x['SIZES']), axis = 1)
stdized_housing_data['SSE'] = stdized_housing_data.apply(lambda x: sse(x['PRICE'],x['PREDICT_PRICE']), axis = 1)
stdized_housing_data['dSSE/da'] = - (stdized_housing_data.PRICE - stdized_housing_data.PREDICT_PRICE)
stdized_housing_data['dSSE/db'] = -(stdized_housing_data.PRICE - stdized_housing_data.PREDICT_PRICE) * stdized_housing_data.SIZES

#print('\nOptimized Data Set Standardization with Error Gradient\n')
#print(stdized_housing_data.sort_values('SIZES'))

totals = stdized_housing_data.sum()

totals_i_want = {'TOTAL_SSE' : totals.loc['SSE'],
				 'TOTAL_dSSE/da' : totals.loc['dSSE/da'],
				 'TOTAL_dSSE/db' : totals.loc['dSSE/db']}

print('\n')
print(totals_i_want)


# write for loop that minimizes the total SSE
# plot sequence

#Axes3D.plot_surface(a,b,stdized_housing_data.SSE)
#plt.show(block=True)


# Step 5: Repeat steps 2 and 3 till further adjustments to weights doesn’t significantly reduce the Error