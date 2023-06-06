# BOJ 2696 중앙값 구하기
#TODO 생각보다 어렵다
#! 강의 보기
import sys

input = sys.stdin.readline 
import heapq

def show_result():
    print(len(result))
    for i in range(len(result)):
        print(result[i], end=' ') #* 10개 단위로 줄바꿈
        if (i + 1) % 10 == 0:
            print()
    print()

for _ in range(int(input())):
    m = int(input())
    data = []
    
    for i in range(m // 10 + 1):
        data.extend(list(map(int, input().split())))
    
    left = [] #* 왼쪽 최대 힙 (원소를 삽입/삭제할 때 음수 부호) 
    right = [] #* 오른쪽 최소 힙
    median = data[0]
    result = [median]
    for i in range(1, m): #*  수열의 원소를 하나씩 확인하며
        if data[i] <= median: heapq.heappush(left, -data[i]) 
        else: heapq.heappush(right, data[i])
        if i % 2 == 0: #*  2개 확인할 때마다
            if len(left) > len(right): #* 왼쪽에서 오른쪽
                heapq.heappush(right, median)
                median = -heapq.heappop(left)
            elif len(left) < len(right): #* 오른쪽에서 왼쪽
                heapq.heappush(left, -median)
                median = heapq.heappop(right)
            result.append(median)
    
    show_result()