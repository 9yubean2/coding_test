#BOJ 1920 수 찾기
n = int(input())
# A = list(map(int, input().split(' ')))    #! 시간 초과
A = set(map(int, input().split(' ')))
m = int(input())
data = list(map(int, input().split(' ')))

for i in data:
    if i in A:  #? in, not in -> return boolean
        print('1')
    else:
        print('0')