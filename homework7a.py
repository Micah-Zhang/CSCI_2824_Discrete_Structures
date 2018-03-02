import time

# Function
def factorMe(N):
	start = time.time()
	p = int(N**0.5)
	if N%2 == 0:
		if p%2 != 0:
			p = p-1
	else:
		if p%2 == 0:
			p = p-1
	while p>=1:
		if N % p == 0:
			q = int(N/p)
			break
		p = p-2
	print(time.time()-start)
	return p,q

# Driver
print(factorMe(22))
print(factorMe(3605282209))
print(factorMe(172410529209361))
