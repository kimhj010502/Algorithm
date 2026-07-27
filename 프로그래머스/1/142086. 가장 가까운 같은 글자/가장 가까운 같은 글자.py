def solution(s):
    alphabet = [-1 for _ in range(26)] # 97~122
    answer = []
    for i in range(len(s)):
        if alphabet[ord(s[i])-97] == -1:
            answer.append(-1)
        else:
            idx = i - alphabet[ord(s[i])-97]
            answer.append(idx)
        alphabet[ord(s[i])-97] = i
    return answer