# https://www.hackerrank.com/challenges/crush/problem
# given a array add value k to indexs [a,b]
# normal brute force wont work for larger arrays and queries
# https://medium.com/@mlgerardvla/hackerrank-array-manipulation-beat-the-clock-using-prefix-sum-92471060035e

	def arrayManipulation(n, queries):   
	    ans=[0 for i in range(n)]
	    for i in queries:
	        ans[i[0]-1]+=i[2]
	        if i[1]<len(ans):
	            ans[i[1]]-=i[2]
	    s=0;maxi=0
	    for i in range(len(ans)):
	        s+=ans[i]
	        maxi=max(maxi,s)
	    return maxi