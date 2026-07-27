def solution(s, n):
    alphabet1 = list(range(ord('a'), ord('z')+1))
    alphabet2 = list(range(ord('A'), ord('Z')+1))

    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        before = ord(s[i])
        after = before + n
        if (before in alphabet1) and (after not in alphabet1):
            after = after - ord('z') + ord('a') - 1
        if (before in alphabet2) and (after not in alphabet2):
            after = after - ord('Z') + ord('A') - 1
        answer += chr(after)
    return answer