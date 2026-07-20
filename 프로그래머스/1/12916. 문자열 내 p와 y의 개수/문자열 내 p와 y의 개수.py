def solution(s):
    cnt = [0, 0]
    for alphabet in s.lower():
        if alphabet == "p":
            cnt[0] += 1
        elif alphabet == "y":
            cnt[1] += 1
    return cnt[0] == cnt[1]