# BOJ 11724 연결 요소의 개수
#! 강의 보기
#TODO Union-Find 자료구조 이용 (합집합 찾기)

import sys
input = sys.stdin.readline

#* 특정 원소가 속한 집합을 찾기
def find_parent(parent, x): 
    #? 루트 노드가 아니라면 
    if parent[x] != x:
        #* 루트 노드를 찾을 때까지 재귀적으로 호출
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


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    a, b = map(int, input().split()) 
    union_parent(parent, a, b) #* a와 b를 연결하기

counter = set() #* 고유한 집합의 수 
for i in range(1, n + 1):
    #* 고유한 집합 번호를 집합에 추가
    counter.add(find_parent(parent, i))
        
print(len(counter))