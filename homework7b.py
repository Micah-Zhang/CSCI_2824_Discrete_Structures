# Function
def sieve_of_E_sum(N):
	# Initialize boolean array to true
	sieve = [True] * N
	# Initialize counter
	p = 2
	while p*p<=N:
		# Necessary b/c python index 0
		# If true, prime has been found
		if sieve[p - 1] == True:
			#print(p)
			# Find all multiples of p and mark False
			i = p * 2
			while i <= N:
				sieve[i-1] = False
				i = i + p
		# Keep incrementing p until another prime is found
		p = p + 1
	p = 2
	sum = 0
	counter = 0
	# Count number and sum of primes < N
	while p<=N:
		if sieve[p-1]:
			counter = counter + 1
			sum = sum + p
			#print(sum)
		p = p + 1
	return counter,sum

# Driver
print(sieve_of_E_sum(5))
