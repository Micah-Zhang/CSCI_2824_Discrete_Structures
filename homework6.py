'''
Name: Micah Zhang
Section: 2 
Instructor: Tony Wong
Date: 10/13/17
'''

# Import the random integer generator 
from random import randint
import time
import matplotlib.pyplot as plt

def mat_vec_gen(n):
	'''
	Function to generate a random matrix of dimension n x n
	and a random vector of length n 
	'''
	A = [[randint(1,100) for ii in range(n)] for jj in range(n)]
	x = [randint(1,100) for ii in range(n)]
	return A, x

'''
Part a: Write a function called mat_vec() that takes as input a
square matrix and a vector of compatible dimensions, and returns
the resulting product vector.
'''
def mat_vec(A,x):
	'''
	Function that takes as input a square matrix
	and a vector of compatible dimensions,
	and returns the resulting product vector.
	'''
	lengthA = len(A)
	lengthx = len(x)
	B = []
	tbeg = time.time()
	for i in range(lengthA):
		rowsize = len(A[i])
		newelement = 0
		for j in range(rowsize):
			newelement = newelement + A[i][j] * x[j]
		B.append(newelement)
	tend = time.time()
	return B, tend-tbeg

'''
Part b: Record the time needed to mutiply an nxn matrix
given a list of sizes. Then make a plot of the matrix
sizes on the horizontal axis versus runtimes to perform
the multiplications on the vertical axis.
'''
sizes = [10,20,40,80,160,320,640,1280,2560,5120,10240]
timing = []
for i in range(len(sizes)):
	A, x = mat_vec_gen(sizes[i])
	B, newtime = mat_vec(A,x)
	timing.append(newtime)
plt.plot(sizes,timing,'blue')
plt.xlabel('size n of nxn matrix')
plt.ylabel('multiplication run-time (s)')
plt.title('size n of nxn matrix vs. multiplication run-time')
plt.show()

'''
Part c: Compute the ratios of timings for consecutive
matrix/vector sizes and store them in the list ratios.
'''
ratios = []
for i in range(len(sizes)-1):
	ratios.append(timing[i+1]/timing[i])
plt.plot(sizes[0:len(sizes)-1],ratios,'blue')
plt.xlabel('size n of nxn matrix')
plt.ylabel('ratios of timings for consecutive matrix/vector sizes')
plt.title('size n of nxn matrix vs. ratios of timings for consecutive matrix/vector sizes')
plt.show()

print(ratios)

'''
ratios: [3.0602409638554215, 3.5354330708661417, 
3.807349665924276, 3.88212927756654, 4.796052135915016, 
3.4545383141160575, 4.098640801422406, 4.017001579891005,
 4.0918421514894066, 3.8974034616506392]
'''
