def tarski(shapes,colors):
	for i in range(len(colors)):
		for j in range(len(colors)):
			if colors[i][j] == 'gray':
				if not shapes[i][j] == 'circle':
					return False
	return True
