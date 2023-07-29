# https://www.hackerrank.com/challenges/append-and-delete
# given starting and desired string, can you convert given string to desired string using only k steps

def appendAndDelete(starting, desired, k):

	if k > len(starting+desired):
		return "Yes"
	common = 0
	for s,d in zip(starting,desired):
		if s==d:
			common += 1
		else:
			break
	moves = len(starting+desired) - (2*common)
	if (k >= moves) and (k-moves) % 2 == 0:
		return "Yes"
	else:
		return "No"

print(appendAndDelete('aba','aba',7))