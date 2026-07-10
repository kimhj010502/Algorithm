def solution(my_string):
    answer = []
    
    # 대문자
    for i in range(26):
        answer.append(my_string.count(chr(i+65)))
    
    # 소문자
    for i in range(26):
        answer.append(my_string.count(chr(i+97)))
    
    return answer