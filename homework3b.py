def first_D_digit_Lucas(D):

	list = [0,1]
	index = 1
	length = 1

	while length < D:
		newnum = list(index) + list(index-1)
		length = len(str(newnum))
		list.append(newnum)
		index = index + 1

	return newnum
