def solution(arr):
    arr.remove(min(arr))
    if len(arr):
        return arr
    return [-1]