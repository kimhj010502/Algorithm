def solution(sides):
    answer = 0
    new_side = [max(sides) - min(sides) + 1]
    while True:
        new_sides = sides + new_side
        if max(new_sides) < sum(new_sides) - max(new_sides):
            answer += 1
            new_side[0] += 1
        else:
            break
    return answer