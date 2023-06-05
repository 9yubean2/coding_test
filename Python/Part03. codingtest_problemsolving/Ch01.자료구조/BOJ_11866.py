# BOJ 11866 요세푸스 문제 0
import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split(' '))

d = deque([i for i in range(1, n + 1)])
result = []

while d:
    for _ in range(k - 1):
        x = d.popleft()
        d.append(x)
    result.append(d.popleft())

print("<", end='')
for i in range(len(result)):
    if i < len(result) - 1:
        print(result[i], end=', ')
    else:
        print(result[i], end='')
print(">")