# BOJ 10773 제로
import sys

input = sys.stdin.readline
k = int(input())

number = []

for _ in range(k):
    data = int(input())

    if data != 0:
        number.append(data)
    else:
        number.pop()

print(sum(number))