def add(num1, num2):
    result = num1 + num2
    if result < 10:
        return str(result), 0
    else:
        return str(result % 10), 1

def solution(a, b):
    if len(a) > len(b):
        b = "0" * (len(a) - len(b)) + b
    elif len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    
    answer = ""
    over_num = 0
    for i in range(len(a)-1, -1, -1):
        result, over_num = add(int(a[i]), int(b[i]) + over_num)
        answer = result + answer
    if over_num == 1:
        answer = "1" + answer
    return answer