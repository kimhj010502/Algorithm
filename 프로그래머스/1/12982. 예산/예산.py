def solution(d, budget):
    d.sort()
    cumsum = 0
    answer = 0
    for i in range(len(d)):
        cumsum += d[i]
        if cumsum <= budget:
            answer = i + 1
    return answer