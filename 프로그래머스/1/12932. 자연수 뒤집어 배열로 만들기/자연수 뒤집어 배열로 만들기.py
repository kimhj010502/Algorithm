def solution(n):
    answer = []
    for num in str(n):
        answer = [int(num)] + answer
    print(answer)
    return answer