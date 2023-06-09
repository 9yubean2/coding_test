# BOJ 10989 수 정렬하기 3
import sys
input = sys.stdin.readline
n = int(input())

#💡 데이터의 개수가 최대 10,000,000개라서 시간 복잡도 O(n)의 정렬 알고리즘 사용
#💡 수의 범위가 1 ~ 10,000이므로 "계수정렬" 사용

array = [0] * 10001

for i in range(n):
    data = int(input())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for _ in range(array[i]):
            print(i)