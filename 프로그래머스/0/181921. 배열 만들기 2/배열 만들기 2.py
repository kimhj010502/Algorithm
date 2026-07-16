def solution(l, r):
    zero_five_set = [{'0'}, {'5'}, {'0', '5'}]
    
    answer = []
    for num in range(l, r+1):
        if set(str(num)) in zero_five_set:
            answer.append(num)
    
    if len(answer):
        return answer
    return [-1]