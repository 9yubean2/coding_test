# BOJ 17298 오큰수
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
stack = []
NGE = [-1] * n


for i in range(n):
    x = arr[i]
    if len(stack) == 0 or stack[-1][0] >= x:    # 내림차순 형태라면
        stack.append((x, i))
    else:
        while len(stack) > 0: # 역방향으로 꺼내기
            previos, index = stack.pop()
            if previos >= x:    # 크거나 같은 이전 원소라면
                stack.append((previos, index))
                break
            else:
                NGE[index] = x # 오큰수 기록
        stack.append((x, i))

for x in NGE:
    print(x, end=' ')