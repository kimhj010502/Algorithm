def ten_to_two(n, num):
    result = []
    
    for i in range(n-1, -1, -1):
        two_num = 2**i
        result.append(num // two_num)
        num = num % two_num
        
    return result
    
    
    

def solution(n, arr1, arr2):
    map1, map2 = [], []
    for i in range(n):
        result1 = ten_to_two(n, arr1[i])
        map1.append(result1)
        result2 = ten_to_two(n, arr2[i])
        map2.append(result2)
    
    answer = []
    for i in range(n):
        tmp = ""
        for j in range(n):
            if map1[i][j] or map2[i][j]:
                tmp = tmp + "#"
            else:
                tmp = tmp + " "
        answer.append(tmp)
    return answer