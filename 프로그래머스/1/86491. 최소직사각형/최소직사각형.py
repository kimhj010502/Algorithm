def solution(sizes):
    h, w = 0, 0
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
        h = max(h, sizes[i][0])
        w = max(w, sizes[i][1])
    return h * w