# 백준 21313
# https://www.acmicpc.net/problem/21313

n = int(input())

if n % 2 == 0:
    print("1 2 " * (n // 2))
else:
    print("1 2 " * (n//2), "3", sep="")


