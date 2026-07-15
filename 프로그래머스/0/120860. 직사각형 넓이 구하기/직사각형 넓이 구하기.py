def solution(dots):
    x = max(dots, key=lambda x: x[0])[0] - min(dots, key=lambda x: x[0])[0]
    y = max(dots, key=lambda x: x[1])[1] - min(dots, key=lambda x: x[1])[1]
    return x * y