# 2D board A of size HxW with H rows and W columns. The board is divided into cells of size 1x1 with each cell indicated by its coordinate(i,j). The cell (i,j) has an integer A(i,j) written on it. To create the structure u have to stack cubes A(i,j) of dimension 1x1x1 on cell (i,j). then calculate its surface area


A = [[1, 2, 1], [3, 2, 2], [4, 3, 4]]


def surfaceArea(A):
    rows = len(A)
    cols = len(A[0])
    maxHeight = max(sum(A, []))
    crossSection = [[[0 for i in range(cols)]for j in range(rows)]for k in range(maxHeight)]
    noOfNeighbours = [[[-1 for i in range(cols)]for j in range(rows)]for k in range(maxHeight)]

    for z in range(1, maxHeight + 1):
        for idxX, i in enumerate(A):
            for idxY, j in enumerate(i):
                if(j >= z):
                    crossSection[z - 1][idxX][idxY] = 1
                else:
                    crossSection[z - 1][idxX][idxY] = 0
    for h, z in enumerate(crossSection):
        for i, v in enumerate(z):
            for j, value in enumerate(v):
                noOfNeigh = 0
                # edges
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    # top
                    if i != 0:
                        if z[i - 1][j] == 1:
                            noOfNeigh += 1
                    # right
                    if j != cols - 1:
                        if z[i][j + 1] == 1:
                            noOfNeigh += 1
                    # bottom
                    if i != rows - 1:
                        if z[i + 1][j] == 1:
                            noOfNeigh += 1
                    # left
                    if j != 0:
                        if z[i][j - 1] == 1:
                            noOfNeigh += 1
                else:
                    noOfNeigh += sum([
                        z[i - 1][j] == 1,
                        z[i][j + 1] == 1,
                        z[i + 1][j] == 1,
                        z[i][j - 1] == 1]
                    )
                if z[i][j] == 1:
                    noOfNeighbours[h][i][j] = noOfNeigh

    noOfNeighbours = sum(noOfNeighbours, [])
    noOfNeighbours = sum(noOfNeighbours, [])
    noOfNeighbours = [4 - i if i != -1 else 0 for i in noOfNeighbours]
    return (sum(noOfNeighbours) + (rows * cols) * 2)


print(surfaceArea(A))
