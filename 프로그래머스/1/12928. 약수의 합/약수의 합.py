def solution(n):
    answer = []
    for i in range(1, n+1):
        if i > (n // i):
            break
        if n % i == 0:
            answer.append(i)
            answer.append(n // i)
    return sum(set(answer))