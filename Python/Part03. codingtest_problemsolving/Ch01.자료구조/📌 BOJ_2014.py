# BOJ 2014 소수의 곱
#! 강의 보기
import sys
import heapq

input = sys.stdin.readline
k, n = map(int, input().split())
data = list(map(int, input().split()))

heap = []   # 우선순위 큐 (최소 힙)
visited = set()     # 이미 처리된 수
max_value = max(data)

for x in data:
    heapq.heappush(heap, x)

for i in range(n - 1):
    element = heapq.heappop(heap)
    for x in data: 
        now = element * x
        if len(heap) >= n and max_value < now:
            continue
        if now not in visited:
            heapq.heappush(heap, now)
            max_value = max(max_value, now)
            visited.add(now)

print(heapq.heappop(heap))
