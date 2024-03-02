matrix = [[2, 4, 0, 0],
          [4, 2, 0, 0],
          [4, 2, 0, 0],
          [0, 0, 0, 0]]
last_matrix = [item[:] for item in matrix]
for line in range(4):
    for i in range(-1, -len(matrix[line]) - 1, -1):
        if matrix[line][i] == 0:
            del matrix[line][i]
            matrix[line].append(0)
print(matrix)
print(last_matrix)
print(last_matrix == matrix)
# matrix = [item[::-1] for item in matrix]
# print(matrix)
