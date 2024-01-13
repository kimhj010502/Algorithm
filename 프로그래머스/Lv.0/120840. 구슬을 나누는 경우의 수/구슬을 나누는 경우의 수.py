def factorial():
    num = [1] * 31 #0! = 1, 1! = 1
    for i in range(2, 31):
        num[i] = num[i-1] * i;
    return num

def solution(balls, share):
    num = factorial()
    answer = num[balls] / (num[balls-share] * num[share])
    return answer