# https://www.hackerrank.com/challenges/extra-long-factorials
# calculate extra long factorials

def extraLongFactorials(n):
    fac = 1
    while n != 1:
    	fac *= n
    	n -= 1
    print(fac)