# 백준 19564
# https://www.acmicpc.net/problem/19564

S = "z" + input()

cnt = 0

for i in range(1, len(S)):
    cnt += S[i] <= S[i - 1]

print(cnt)




