def is_even(n):
    if n**0.5 % 1 == 0:
        return -1
    return 1

def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        answer += is_even(n) * n
    return answer