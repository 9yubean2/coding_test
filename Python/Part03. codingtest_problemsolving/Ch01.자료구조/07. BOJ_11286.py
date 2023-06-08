# BOJ 11286 절댓값 힙
#TODO: heapq 라이브러리로 우선순위 큐를 활용하여 해결
import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
result = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if len(heap) == 0:
            print(0)
        else: 
            absolute, original = heapq.heappop(heap)
            print(original)