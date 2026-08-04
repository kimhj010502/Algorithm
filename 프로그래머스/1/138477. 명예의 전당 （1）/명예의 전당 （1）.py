def solution(k, score):
    answer = []
    legend = []
    for i in range(len(score)):
        if i < k:
            legend.append(score[i])
        elif score[i] > legend[-1]:
            legend.pop()
            legend.append(score[i])
        legend.sort(reverse=True)
        answer.append(legend[-1])
    return answer