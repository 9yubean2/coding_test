# BOJ 1427 소트인사이드
import sys
input = sys.stdin.readline
n = input().strip()
arr = []
for i in range(len(n)):
    arr.append(int(n[i]))
arr.sort(reverse=True)

for i in arr:
    print(i, end='')
