# https://www.hackerrank.com/challenges/sparse-arrays
# given a list of strings and a list of strings which are queries, print how many times a query apperears in the list of strings

def matchingStrings(stringList, queries):
	
	counts = []
	for q in queries:
		counts.append(stringList.count(q))
	return counts

print(matchingStrings(['ab','abc','ab'], ['ab','abc','bc']))