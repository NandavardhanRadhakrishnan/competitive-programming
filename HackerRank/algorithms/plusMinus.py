# https://www.hackerrank.com/challenges/plus-minus
# given a array of ints find the ratio of positive, negative and zeros

def plusMinus(arr):
	p,n,z=0,0,0
	for i in arr:
		if i>0:
			p+=1
		elif i<0:
			n+=1
		else:
			z+=1
	print(p/len(arr))
	print(n/len(arr))
	print(z/len(arr))

plusMinus([1,1,-2,-2,0])