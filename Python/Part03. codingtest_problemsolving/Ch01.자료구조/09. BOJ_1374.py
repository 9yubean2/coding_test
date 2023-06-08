# BOJ 1374 강의실
#TODO: 우선순위 큐로 해결 가능 => heapq
import sys
import heapq
input = sys.stdin.readline
n = int(input())
lectures = []
for _ in range(n):
    id, start, end = map(int, input().split())
    heapq.heappush(lectures, (start, end))      #* 우선순위 큐니까 자동으로 정렬

heap = [] #* 강의실

end = heapq.heappop(lectures)[1]    #* 제일 먼저 시작하는 강의의 종료시간
heapq.heappush(heap, end)
answer = 1

for i in range(n - 1):
    new_start, new_end = heapq.heappop(lectures)
    end = heapq.heappop(heap)

    if new_start < end: #? 강의 시간이 겹치면
        heapq.heappush(heap, end)   #* 기존 강의실 유지
        heapq.heappush(heap, new_end)   #* 새로운 강의실 추가
        answer += 1
    else:
        heapq.heappush(heap, new_end)

print(answer)
