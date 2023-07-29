# https://www.hackerrank.com/challenges/breaking-best-and-worst-records
# given scores as a array of ints, find the number of times best and worst record is broken

def breakingRecords(scores):
	best,worst = scores[0],scores[0]
	bRecord,wRecord = 0,0
	for i in scores:
		if (i>best):
			bRecord += 1
			best = i
		if (i<worst):
			wRecord += 1
			worst = i
	return [bRecord,wRecord]

print(breakingRecords([10,5,20,20,4,5,2,25,1]))