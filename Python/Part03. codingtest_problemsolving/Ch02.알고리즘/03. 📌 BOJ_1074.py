# BOJ 1074 Z
import sys
input = sys.stdin.readline

n,r,c = map(int, input().split())
result = 0

def solve(n, x, y):
    global result
    if x == r and y == c:
        print(result)
        exit(0)
    if n == 1:
        result += 1
        return
    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return
    temp = n // 2
    solve(temp, x, y)
    solve(temp, x, y + temp)
    solve(temp, x + temp, y)
    solve(temp, x + temp, y + temp)

solve(2 ** n, 0, 0)
print(result)