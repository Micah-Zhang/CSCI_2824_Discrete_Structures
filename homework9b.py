import math

# Function
def binom_product(a,b,n):
	prod = 1
	for i in range(0,n+1):
		bico = math.factorial(n)/(math.factorial(n-i)*math.factorial(i))
		new = bico*math.pow(a,n-i)*math.pow(b,i)
		prod = prod * new
	return prod

# Driver
print(binom_product(2,-1,3))
