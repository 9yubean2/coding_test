# BOJ 11650 좌표 정렬하기
import sys
input = sys.stdin.readline
n = int(input())

positions = []

for _ in range(n):
    x, y = map(int, input().split())
    positions.append((x, y))

#* key 속성 설정 없이 기본 정렬 라이브러리 사용
positions = sorted(positions)   #? sorted()는 기본적으로 튜플의 인덱스 순서대로 오름차순 정렬

for position in positions:
    print(position[0],position[1])