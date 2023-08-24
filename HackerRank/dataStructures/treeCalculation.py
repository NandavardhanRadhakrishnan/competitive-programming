# https://www.hackerrank.com/challenges/kittys-calculations-on-a-tree
# given input form a tree, then calculate distance between nodes for given queries
# https://programs.programmingoneonone.com/2021/05/hackerrank-kittys-calculations-on-a-tree-solution.html
# ridiculous test cases, 10k+ nodes with 1k+ queries. below code works perfectly well, but they had to destroy it with some bs 

from itertools import combinations

def shortestDist(pairs,numOfNodes):
	dist = [[float('inf') for _ in range(numOfNodes)] for _ in range(numOfNodes)]
	for pair in pairs:
		pair[0] -= 1
		pair[1] -= 1

	for edge in pairs:
		n1,n2 = edge
		dist[n1][n2] = 1
		dist[n2][n1] = 1

	for k in range(numOfNodes):
		for i in range(numOfNodes):
			for j in range(numOfNodes):
				dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

	for i in range(numOfNodes):
		dist[i][i] = 0
	return dist

def querySolver(a,b,dist):
	return(a*b*dist[a-1][b-1])%((10**9)+7)

n,q = list(map(int,input().split()))
nodePairs = []
for _ in range(n-1):
	nodePairs.append(list(map(int,input().split())))

queriesSet = []
for _ in range(q):
	i = input()
	querySet = list(map(int,input().split()))
	if len(querySet) < 2:
		querySet.append(querySet[0])
	queriesSet.append(querySet)

d = shortestDist(nodePairs, n)

queriesSet=[[2,4],[1,1],[2,4,5]]

for query in queriesSet:
	s =0
	for qset in combinations(query,2):
		s+=querySolver(qset[0],qset[1], d)
	print(s)