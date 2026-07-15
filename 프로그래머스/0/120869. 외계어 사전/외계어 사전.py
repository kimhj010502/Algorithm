def solution(spell, dic):
    for i in range(len(dic)):
        if len(dic[i]) == len(spell) and set(dic[i]) == set(spell):
            return 1
    return 2