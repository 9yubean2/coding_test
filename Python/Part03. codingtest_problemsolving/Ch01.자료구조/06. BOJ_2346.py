# BOJ 2346 풍선 터뜨리기
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split(' ')))
d = deque([(i, idx) for idx, i in enumerate(arr)])

result = []

while d:
    x = d.popleft()
    result.append(x[1] + 1)
    if len(result) == n:
        break
    if x[0] > 0:
        for _ in range(x[0] - 1):
            x = d.popleft()
            d.append(x)
    else:
        for _ in range(abs(x[0])):
            x = d.pop()
            d.appendleft(x)

for i in result:
    print(i, end=' ')
