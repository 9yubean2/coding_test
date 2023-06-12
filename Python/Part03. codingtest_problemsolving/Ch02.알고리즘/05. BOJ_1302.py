# BOJ 1302 베스트 셀러 (https://www.acmicpc.net/problem/1302)
import sys

input = sys.stdin.readline
n = int(input())
books = dict()

for _ in range(n):
    book = input().strip()
    if  book not in books:
        books[book] = 1
    else:
        books[book] += 1

target = max(books.values())
array = []

for book, number in books.items():
    if number == target:
        array.append(book)

print(sorted(array)[0])