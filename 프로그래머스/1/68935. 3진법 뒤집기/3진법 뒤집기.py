def ten_to_three(n):
    answer = ''
    while(n):
        answer = str(n % 3) + answer
        n = n // 3
    return answer

def solution(n):
    three = ten_to_three(n)
    three_reverse = three[::-1]
    ten = int(three_reverse, 3)
    return ten