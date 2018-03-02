# Function
def count_rectangles(m,n):
	sum = 0
	if(n < m):
		m,n = n,m
	return int(m*(m+1)*n*(n+1)/4)

# Driver
print(count_rectangles(1,1))
print(count_rectangles(2,1))
print(count_rectangles(2,2))

#(1 1) 1
#(2 1) 3
#(2 2) 9
