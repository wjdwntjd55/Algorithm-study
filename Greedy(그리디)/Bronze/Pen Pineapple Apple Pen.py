# 백준 15881
# https://www.acmicpc.net/problem/15881

N = int(input())
N_list = list(input())

N_list.extend([0] * 1000000)
i, cnt = 0, 0

while (i < N):
    if(N_list[i] == 'p' and N_list[i+1] == 'P' and N_list[i+2] == 'A' and N_list[i+3] == 'p'):
        N_list[i+3] = 0
        cnt += 1

    i += 1

print(cnt)

# 방범 2
# n = int(input())
# ppap = input()
# arr = list(ppap)
# num=0
# for i in range(n):
#     if i+4<=n:
#         if arr[i]=='p':
#             if arr[i+1]=='P':
#                 if arr[i+2]=='A':
#                     if arr[i+3]=='p':
#                         num+=1
#                         arr[i+3]='Z'
#
# print(num)








