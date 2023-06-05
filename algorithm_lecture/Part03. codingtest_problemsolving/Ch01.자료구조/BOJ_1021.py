# BOJ 1021 회전하는 큐
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split(' '))
d = deque([i for i in range(1, n + 1)]) #? 1부터 n까지를 원소로 가지는 덱 생성
targets = list(map(int, input().split(' ')))
cnt = 0 #? 회전 수

for target in targets:
    index = d.index(target)
    if index <= len(d) // 2:    #* 왼쪽으로 돌리는 게 빠른 경우
        for i in range(index):
            x = d.popleft()
            d.append(x)
            cnt += 1
    else:   #* 오른쪽으로 돌리는 게 빠른 경우
        for i in range(len(d) - index):
            x = d.pop()
            d.appendleft(x)
            cnt += 1
    d.popleft() #? 원소 추출

print(cnt)