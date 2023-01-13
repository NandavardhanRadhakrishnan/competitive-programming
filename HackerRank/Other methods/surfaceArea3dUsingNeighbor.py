A = [[1, 2, 1]]


def surfaceArea(A):
    rows = len(A)
    cols = len(A[0])

    Sum = 0
    for i, Xval in enumerate(A):
        for j, val in enumerate(Xval):

            # top left corner
            if (i == 0 and j == 0):
                Sum += 2 * val
                Sum += abs(val - A[i + 1][j])
                Sum += abs(val - A[i][j + 1])

            # bottom right corner
            elif (i == rows - 1 and j == cols - 1):
                Sum += 2 * val

            # bottom left corner
            elif(i == rows - 1 and j == 0):
                Sum += 2 * val
                Sum += abs(val - A[i][j + 1])

            # top right corner
            elif(i == 0 and j == cols - 1):
                Sum += 2 * val
                Sum += abs(val - A[i + 1][j])

            # top edge
            elif(i == 0 and (j > 0 and j < cols - 1)):
                Sum += val
                Sum += abs(val - A[i + 1][j])
                Sum += abs(val - A[i][j + 1])

            # left edge
            elif(j == 0 and (i > 0 and i < rows - 1)):
                Sum += val
                Sum += abs(val - A[i + 1][j])
                Sum += abs(val - A[i][j + 1])

            # bottom edge
            elif(i == rows - 1 and (j > 0 and j < cols - 1)):
                Sum += val
                Sum += abs(val - A[i][j + 1])

            # right edge
            elif(j == cols - 1 and (i > 0 and i < rows - 1)):
                Sum += val
                Sum += abs(val - A[i + 1][j])

            # center
            else:
                Sum += abs(val - A[i + 1][j])
                Sum += abs(val - A[i][j + 1])
    Sum += (rows * cols) * 2
    return Sum


print(surfaceArea(A))
