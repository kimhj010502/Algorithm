def solution(arr):
    answer = arr
    nrow, ncol = len(arr), len(arr[0])
    if nrow < ncol:
        for _ in range(ncol - nrow):
            answer.append([0 for _ in range(ncol)])
    elif nrow > ncol:
        for i in range(nrow):
            answer[i] = answer[i] + [0 for _ in range(nrow - ncol)]
    return answer