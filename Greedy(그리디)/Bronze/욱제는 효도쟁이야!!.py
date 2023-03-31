# 백준 14487
# https://www.acmicpc.net/problem/14487

N = int(input())
charge = list(map(int, input().split()))
total = 0
start = max(charge)

for i in charge:
    total += i

print(total - start)

