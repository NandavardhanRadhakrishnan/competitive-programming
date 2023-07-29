# https://www.hackerrank.com/challenges/birthday-cake-candles
# for a array of candles given by array of ints where the int is the height, you can only blow out the tallest candles, return number of candles you can blow out

def birthdayCakeCandles(candles):
	return(candles.count(max(candles)))

print(birthdayCakeCandles([3,4,2,4]))