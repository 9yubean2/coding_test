# BOJ 2798 블랙잭
n, m = list(map(int,input().split(' ')))
cards = list(map(int,input().split(' ')))

result = 0
# length = len(cards) # n 이잖아ㅇㅅㅇ

cnt = 0
for i in range(0, n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m:
                result = max(result, sum)

print(result)