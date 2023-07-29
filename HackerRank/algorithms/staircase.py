# https://www.hackerrank.com/challenges/staircase
# print a staircase of n step going climbing from left to right

def staircase(n):
	for i in range(1,n+1):
		print(" "*(n-i),end="")
		print("#"*i,end="\n")

staircase(10)