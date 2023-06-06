# BOJ 20040 사이클 게임
#! 강의 보기
#TODO Union-Find 자료구조 이용 (합집합 찾기)

import sys

input = sys.stdin.readline

#* 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    #? 루트 노드가 아니라면
    if parent[x] != x:
        #* 루트 노드 찾을 때까지 재귀적으로 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#* 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [0] * n
for i in range(n):
    parent[i] = i

cycle = False #* 사이클 발생 여부

for i in range(m):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        print(i + 1)
        break
    else:
        union_parent(parent, a, b)

if not cycle:
    print(0)

