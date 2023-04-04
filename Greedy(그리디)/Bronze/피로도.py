# 백준 22864
# https://www.acmicpc.net/problem/22864
A, B, C, M = map(int, input().split())

time = 0
tired = 0
works = 0

while(time < 24):
    if (M - tired) >= A:
        tired += A
        works += B
    else:
        tired -= C
        if tired < 0:
            tired = 0
    time += 1

print(works)

