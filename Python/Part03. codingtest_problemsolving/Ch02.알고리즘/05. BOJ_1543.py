# BOJ 1543 문서 검색
import sys
input = sys.stdin.readline
document = input().strip()
word = input().strip()

print(len(document.split(word)) - 1)

'''
document = input()
word = input()
index = 0
result = 0
while len(document) - index >= len(word):
    if document[index:index + len(word)] == word: # 문서에서 보고 있는 단어가 찾고자 하는 단어인 경우
        result += 1
        index += len(word)
    else:
        index += 1
print(result)
'''