def get_divisor_num(n):
    if n == 1:
        return 1
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if (n**0.5) == i:
            cnt += 1
        elif n % i == 0:
            cnt += 2
    return cnt


def solution(number, limit, power):
    answer = 0
    for n in range(1, number+1):
        div_num = get_divisor_num(n)
        if div_num <= limit:
            answer += div_num
        else:
            answer += power
    return answer