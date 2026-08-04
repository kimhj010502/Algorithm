def solution(food):
    food1 = ''
    for i in range(1, len(food)):
        food1 += str(i) * (food[i] // 2)
    food2 = food1[::-1]
    return food1 + '0' + food2