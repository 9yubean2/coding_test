# BOJ 2751 수 정렬하기 2
import sys
import heapq

input = sys.stdin.readline
heap = []
n = int(input())

for _ in range(n):
    heapq.heappush(heap, int(input()))

for _ in range(n):
    print(heapq.heappop(heap))


'''#💡 병합 정렬
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j] 
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right): 
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)'''