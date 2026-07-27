def solution(n, m):
    max_num = 1
    for i in range(1, min(n, m)+1):
        if (n % i == 0) and (m % i == 0):
            max_num = i
    min_num = (n * m) / max_num
    return [max_num, min_num]