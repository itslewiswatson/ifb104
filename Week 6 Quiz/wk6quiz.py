matrix = [
	[1, 2, 3, 4, 5],
	[6, 7, 8, 9, 10],
	[11, 12, 13, 14, 15],
	[16, 17, 18, 19, 20],
	[21, 22, 23, 24, 25]
]

diagonal = []
last_column = len(matrix[0]) - 1
for row in [0, 1, 2, 3, 4]:
	diagonal.append(matrix[row][last_column - row])

print(diagonal)