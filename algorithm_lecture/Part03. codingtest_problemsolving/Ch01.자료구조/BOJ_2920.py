#  BOJ 2920 음계
input = list(map(int,input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if input[i] > input[i - 1]:
        descending = False
    elif input[i] < input[i - 1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")