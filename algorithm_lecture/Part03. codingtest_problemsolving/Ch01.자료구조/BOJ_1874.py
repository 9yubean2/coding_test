# BOJ 1874 스택 수열
n = int(input())

cnt = 1
stack = []
result = []

for i in range(1, n + 1): # 데이터 개수만큼 반복
    data = int(input())
    while cnt <= data: # 입력받은 데이터에 도달할 때까지 삽입
        stack.append(cnt)
        cnt += 1
        result.append('+')
    if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때
        stack.pop()
        result.append('-')
    else: # 불가능한 경우
        print('NO')
        exit(0)

print ('\n'.join(result)) # 가능한 경울