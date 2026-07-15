def solution(cards1, cards2, goal):
    n1, n2 = 0, 0
    for i in range(len(goal)):
        if (n1 < len(cards1)) and (goal[i] == cards1[n1]):
            n1 += 1
        elif (n2 < len(cards2)) and (goal[i] == cards2[n2]):
            n2 += 1
        else:
            return "No"
    return "Yes"