# BOJ 1715 카드 정렬하기
import sys
import heapq

input = sys.stdin.readline
n = int(input())
cards = []

for _ in range(n):
    card = int(input())
    heapq.heappush(cards, card)

result = 0

while len(cards) != 1:
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)
    sum_value = first + second
    result += sum_value
    heapq.heappush(cards, sum_value)

print(result)