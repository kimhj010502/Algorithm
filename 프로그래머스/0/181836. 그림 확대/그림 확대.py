def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        row = ""
        for j in range(len(picture[i])):
            row = row + picture[i][j] * k
        for j in range(k):
            answer.append(row)
    return answer