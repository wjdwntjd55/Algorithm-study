from itertools import permutations

# 백준 25176
# https://www.acmicpc.net/problem/25176

# 같은숫자가 붙어있어야 최솟값이 된다
# 만약, n = 4 이면
# 11 22 33 44
# 4 * 3 * 2 * 1 = 24 = 4!

# 방법1. 순열(permutations) 이용

n=int(input())
arr=[]
for i in range(n):
    arr.append(i)

count=0
for i in permutations(arr,n):
    count+=1

print(count)

# 방법2. 순열 개념 이용
# n = int(input())
# cnt = 1
# for i in range(1, n+1):
#     cnt *= i
#
# print(cnt)