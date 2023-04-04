# 백준 14720
# https://www.acmicpc.net/problem/14720

N = int(input())

milk = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if milk[i] == cnt % 3:
        cnt += 1

print(cnt)


