import time

# Function
def goldbackCheck(N):
	start = time.time()
	# Set size of array
	#limit = int(N/2)
	limit = N
	# Initialize boolean array to true
	sieve = [True] * limit
	# Initialize counter
	p = 2
	while p<=limit:
		# Necessary b/c python index 0
		# If true, prime has been found
		if sieve[p - 1] == True:
			# Find all multiples of p and mark False
			i = p * 2
			while i <= limit:
				sieve[i-1] = False
				i = i + p
		# Keep incrementing p until another prime is found
		p = p + 1
	p = 2
	while p <= limit:
		if sieve[p-1]:
			q = N-p
			if sieve[q-1]:
				break
		p = p + 1
	print(time.time()-start)
	return p,q

# Driver
print(goldbackCheck(940606))
