# BOJ 7662 이중 우선순위 큐
#! 강의 듣기
import sys
import heapq

def pop(heap):  #? heap과 deleted는 global 변수
    while len(heap) > 0:
        data, id = heapq.heappop(heap)
        if not deleted[id]: #* 삭제한 적이 없는 원소
            deleted[id] = True
            return data
    return None #? 삭제할 원소가 없으면 None 반환

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    k = int(input())
    min_heap = []   #* 최소 힙 (heapq는 최소 힙)
    max_heap = []   #* 최대 힙 (삽입/삭제 시 음수로 삽입)
    current = 0     #* 삽입할 원소의 인덱스 값
    deleted = [False] * (k + 1)
    for i in range(k):
        command = input().split()
        operator, data = command[0], int(command[1])
        if operator == 'D':
            if data == -1: pop(min_heap)
            elif data == 1: pop(max_heap)
        elif operator == 'I':
            heapq.heappush(min_heap, (data, current))
            heapq.heappush(max_heap, (-data, current))
            current += 1
    max_value = pop(max_heap)
    if max_value == None: print("EMPTY")
    else:
        heapq.heappush(min_heap, (-max_value, current))
        print(-max_value, pop(min_heap))