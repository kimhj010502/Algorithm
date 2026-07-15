def solution(x):
    sum_num = 0
    for n in str(x):
        sum_num += int(n)
    
    if x % sum_num == 0:
        return True
    else:
        return False