def solution(numbers, k):
    cnt = 2 * (k-1) #공이 지나친 사람 수
    idx = cnt % len(numbers) + 1
    return idx