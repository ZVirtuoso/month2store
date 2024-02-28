matrix = [[0, 0, 0, 5],
         [0, 18, 6, 0],
         [7, 0, 0, 0],
         [0, 0, 13, 0]]

matrix = [[x for x in item] for item in zip(*matrix)]
print(matrix)

# matrix = [item[::-1] for item in matrix]
# print(matrix)