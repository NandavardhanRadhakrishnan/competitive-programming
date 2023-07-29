# https://www.hackerrank.com/challenges/the-grid-search
# given matrix G and P, return if P is inside G

def gridSearch(G,P):
	for row in range(len(G) - len(P) + 1):
		for col in range(len(G[0]) - len(P[0]) + 1):
			for i in range(len(P)):
				if P[i] != G[row + i][col : col + len(P[0])]:
					found = 'NO'
					break
				else:
					found = 'YES'
			if found == 'YES':
				return found
	return found




print(gridSearch(['1234', '4321', '9999', '9999'], ['12','21']))