def operation(num1, op, num2):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2

    
def solution(quiz):
    answer = []
    
    for i in range(len(quiz)):
        num1, op, num2, temp, num3  = quiz[i].split(' ')
        [num1, num2, num3] = map(int, [num1, num2, num3])
        
        if operation(num1, op, num2) == num3:
            answer.append('O')
        else:
            answer.append('X')
    
    return answer