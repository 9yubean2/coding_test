# BOJ 10828 스택
import sys
input = sys.stdin.readline 

n = int(input())    #! 기본 input으로 입력값을 읽으면 시간초과
stack = []

for _ in range(n):
    command = input().strip().split(' ')    #! sys로 읽었기 때문에 줄바꿈 기호는 자르기
    
    if command[0] == 'push':
        stack.append(int(command[1]))
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    else:
        if stack:
            print(stack[-1])
        else:
            print('-1')
