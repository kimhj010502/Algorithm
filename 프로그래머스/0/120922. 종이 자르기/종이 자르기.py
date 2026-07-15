def solution(M, N):
    sides = [M, N]
    sides.sort()
    answer = (sides[0] - 1) + (sides[1] - 1) * sides[0]
    return answer