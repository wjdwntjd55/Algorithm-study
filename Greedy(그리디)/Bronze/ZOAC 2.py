# 백준 18238번
# https://www.acmicpc.net/problem/18238

# 문자를 아스키 코드로 변환
# 알파벳은 총 26개
# A ~ Z 의 아스키 코드 범위 : 65 ~ 90

words = list(input())

start = 'A'
time = 0

for i in words:
    left = ord(start) - ord(i)
    right = ord(i) - ord(start)

    if left < 0:
        left += 26
    elif right < 0:
        right += 26

    time += min(left, right)
    start = i

print(time)



