# BOJ 2953 나는 요리사다
import sys
input = sys.stdin.readline
participants = []
for _ in range(5):
    participants.append(list(map(int, input().split(' '))))

scores = []

for idx, data in enumerate(participants):
    scores.append((idx, sum(data)))

result = max(scores, key=lambda x:x[1])
print(f"{result[0] + 1} {result[1]}")