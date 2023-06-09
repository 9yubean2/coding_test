# BOJ 2750 수 정렬하기
import sys
input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)

arr.sort()
for i in arr:
    print(i)

'''
#TODO 선택 정렬 알고리즘
import sys
input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

for i in arr:
    print(i)
'''