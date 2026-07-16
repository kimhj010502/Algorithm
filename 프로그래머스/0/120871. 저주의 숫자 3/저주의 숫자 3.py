def solution(n):
    answer = {}
    three_num = 0
    for num in range(1, n+1):
        while True:
            if (three_num % 3 == 0) or ('3' in str(three_num)):
                three_num += 1
            else:
                break
        answer[num] = three_num
        three_num += 1
    return answer[n]