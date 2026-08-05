def solution(name, yearning, photo):
    name_dict = {}
    for i in range(len(name)):
        name_dict[name[i]] = yearning[i]
    print(name_dict)
    
    answer = []
    for i in range(len(photo)):
        score = 0
        for j in range(len(photo[i])):
            try:
                score += name_dict[photo[i][j]]
            except:
                continue
        answer.append(score)
    return answer