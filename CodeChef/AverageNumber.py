# https://www.codechef.com/problems/AVG
# sequence of n+k numbers
t=int(input())
while(t):
    t = t-1
    n, k, v = list(map(int, input().split()))
    nums =list(map(int, input().split()))
    if sum(nums)/(n+k) > v:
        print(-1)
    elif (sum(nums)*k)%(n+k) != 0:
        print(-1)
    else:
        print(int((v*(n+k)-sum(nums))/k))