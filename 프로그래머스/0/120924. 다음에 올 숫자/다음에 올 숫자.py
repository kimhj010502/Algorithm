def solution(common):
    is_minus = True
    d = common[1] - common[0]
    for i in range(2, len(common)):
        if d != (common[i] - common[i-1]):
            is_minus = False
            break
    
    if is_minus: # 등차수열
        answer = common[-1] + d
    else: # 등비수열
        r = common[1] / common[0]
        answer = common[-1] * r
    return answer
    