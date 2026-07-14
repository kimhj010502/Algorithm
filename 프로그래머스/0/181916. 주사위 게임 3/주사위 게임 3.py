def solution(a, b, c, d):
    num_count = []
    for i in range(1, 7):
        num_count.append([i, [a, b, c, d].count(i)])
    num_count.sort(key=lambda x: x[1], reverse=True)

    if num_count[0][1] == 4:
        p = num_count[0][0]
        answer = 1111 * p
    elif num_count[0][1] == 3:
        p = num_count[0][0]
        q = num_count[1][0]
        answer = (10 * p + q)**2
    elif num_count[0][1] == 2:
        if num_count[1][1] == 2:
            p = num_count[0][0]
            q = num_count[1][0]
            answer = (p + q) * abs(p - q)
        else:
            q = num_count[1][0]
            r = num_count[2][0]
            answer = q * r
    elif num_count[0][1] == 1:
        answer = min([a, b, c, d])
    return answer