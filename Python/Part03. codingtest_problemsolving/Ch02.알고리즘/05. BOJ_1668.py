# BOJ 1668 트로피 진열
n = int(input())
trophies = []
for _ in range(n):
    trophies.append(int(input()))

left_min = trophies[0]
right_min = trophies[-1]

left_result = 1
right_result = 1

for trophy in trophies:
    if trophy > left_min:
        left_min = trophy
        left_result += 1

for trophy in reversed(trophies):
    if trophy > right_min:
        right_min = trophy
        right_result += 1

print(left_result)
print(right_result)
