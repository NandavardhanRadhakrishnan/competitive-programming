# https://www.hackerrank.com/challenges/mini-max-sum
# given a int array of lenght 5, find the min and max sum by taking exactly 4 of 5 ints

def minMaxSum(arr):
	arr.sort()
	print(sum(arr[:4]),sum(arr[1:]))

minMaxSum([1,2,3,4,5])