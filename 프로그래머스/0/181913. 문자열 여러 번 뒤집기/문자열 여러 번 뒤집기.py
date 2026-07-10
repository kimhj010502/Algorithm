def reverse_string(my_string, s, e):
    result = my_string[:s]
    for i in range(e, s-1, -1):
        result = result + my_string[i]
    result = result + my_string[e+1:]
    return result


def solution(my_string, queries):
    answer = my_string
    for q in queries:
        answer = reverse_string(answer, q[0], q[1])
    return answer