def check_proposition(E):
	if not E:
		return True
	counter = 0;
	counter2 = 0;
	for i in range(len(E)):
		if not E[i] % 2:
			counter += 1
			for j in range(len(E)):
				if E[i] == 2 * E[j]:
					counter2 += 1
					break
	print(counter,counter2)
	if counter != 0 and counter == counter2:
		return True
	else:
		return False
def main():
	#E = list(range(6))
	E = [1,1,1,1,1,1,1,1]
	print(E)
	print(check_proposition(E))

if __name__ == "__main__":
	main()
