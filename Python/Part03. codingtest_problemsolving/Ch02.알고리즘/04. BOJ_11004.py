# BOJ 11004 K 번째 수
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
array = list(map(int,input().split()))
array = sorted(array)
print(array[k - 1])