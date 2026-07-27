def solution(s):
    word_list = s.split(" ")
    answer = ''
    for word in word_list:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    return answer[:-1]