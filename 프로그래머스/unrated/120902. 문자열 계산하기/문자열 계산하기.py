def solution(my_string):
    num_list = list(my_string.split())
    
    answer = int(num_list[0])
    
    i = 1
    while (i < len(num_list)):
        #덧셈 연산
        if num_list[i] == '+':
            answer += int(num_list[i+1])
        
        #뺄셈 연산
        elif num_list[i] == '-':
            answer -= int(num_list[i+1])
        
        i += 2

    return answer