# https://www.hackerrank.com/challenges/bigger-is-greater/
# given a word find smallest word which is bigger than the given word, with only swapping letters, if not possible then return "no answer"

# algorithm used next permutation
# https://medium.com/@studying1999/bigger-is-greater-problem-comprehensive-explanation-b2ea7eacc0b2

for _ in range(int(input())):
    s = input()
    s = list(s[::-1])
    done = 0
    for i in range(1,len(s)):
        if s[i-1] > s[i]:
            for j in range(i):
                if s[j] > s[i]:
                    s[j],s[i] = s[i],s[j]
                    s = sorted(s[:i])[::-1] + s[i:]
                    print("".join(s[::-1]))
                    break
            break
    else:
        print("no answer")