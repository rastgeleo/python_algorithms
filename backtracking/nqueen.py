
def is_valid(matrix, row, col):
    for i in range(row):
        # check the same column
        if matrix[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        # check left upper diagonal
        if matrix[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(matrix))):
        # check right upper diagonal
        if matrix[i][j] == 1:
            return False
    return True


def dfs(matrix, row):
    if row >= len(matrix):
        return True
    for i in range(len(matrix)):
        if is_valid(matrix, row, i):
            # if valid place a queen
            matrix[row][i] = 1
            # and check the next row recursively return True if they're fine
            if dfs(matrix, row+1) == True:
                return True
            # if not returned, back to the previous status.
            matrix[row][i] = 0
    return False


def find_n_queen(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    if dfs(matrix, 0):
        return matrix
    else:
        return False

for row in find_n_queen(8):
    print(row)