def solution(score):
    avg_score = []
    for i in range(len(score)):
        avg_score.append(sum(score[i])/2)

    answer = [sorted(avg_score, reverse=True).index(avg_score[i]) + 1 for i in range(len(score))]
    return answer