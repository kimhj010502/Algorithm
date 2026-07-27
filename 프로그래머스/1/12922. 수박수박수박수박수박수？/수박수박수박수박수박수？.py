def solution(n):
    soobak = ['수', '박']
    answer = ''
    for i in range(n):
        answer = answer + soobak[i % 2]
    return answer