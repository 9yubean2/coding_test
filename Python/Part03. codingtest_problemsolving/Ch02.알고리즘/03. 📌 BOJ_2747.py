# BOJ 2747 피보나치 수
#🔥 이렇게 하면 시간 초과 => 재귀적 구현의 한계
'''def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(int(input())))'''

n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)