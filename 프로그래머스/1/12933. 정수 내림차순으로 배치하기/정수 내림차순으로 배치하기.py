def solution(n):
    answer = []
    for num in str(n):
        answer.append(num)
    answer.sort(reverse=True)
    
    result = ""
    for i in range(len(answer)):
        result = result + answer[i]
    return int(result)
