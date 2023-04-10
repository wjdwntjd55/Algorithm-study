# 1. 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1 부터 n 까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 2. 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n 이 1 이하인 경우 1을 반환
        return 1

    # n! = n * (n-1)! 를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
# 둘다 결과는 120 = 5 * 4 * 3 * 2 * 1
print("1. 반복적으로 구현 : ", factorial_iterative(5))
print("2. 재귀적으로 구현 : ", factorial_recursive(5))
