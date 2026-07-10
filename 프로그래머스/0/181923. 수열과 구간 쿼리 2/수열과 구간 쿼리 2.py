def get_min(arr, s, e, k):
    min_value = 1e10
    for i in range(s, e+1):
        if arr[i] > k:
            min_value = min(min_value, arr[i])
    if min_value == 1e10:
        return -1
    return min_value
        

def solution(arr, queries):
    answer = []
    for q in queries:
        answer.append(get_min(arr, q[0], q[1], q[2]))
    return answer