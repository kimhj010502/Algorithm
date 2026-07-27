def solution(s):
    l = len(s)
    if l % 2 == 1:
        answer = s[l//2:l//2+1]
    else:
        answer = s[l//2-1:l//2+1]
    return answer