# BOJ 1325 효율적인 해킹
#🔥 시간 초과..?
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)

def bfs(v):
    q = deque([v])
    visited = [False for _ in range(n+1)]
    visited[v] = True
    count = 1
    
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]: 
                q.append(e)
                visited[e] = True
                count += 1
    return count

result = []
max_value = 1

for i in range(1, n + 1):
    count = bfs(i)
    if count > max_value:
        max_value = count
        result.clear()
        result.append(i)
    elif count == max_value:
        result.append(i)

print(*result)