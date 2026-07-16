def solution(num, total):
    m = int(total / num)
    if total % num == 0:
        answer = list(range(m - num // 2, m + num // 2 + 1))
    else:
        answer = list(range(m - num // 2 + 1, m + num // 2 + 1))
    return answer