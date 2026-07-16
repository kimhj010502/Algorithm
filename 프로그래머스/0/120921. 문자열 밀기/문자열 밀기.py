def solution(A, B):
    if A == B:
        return 0
    for i in range(1, len(A)):
        new_A = A[-i:] + A[:len(A)-i]
        if new_A == B:
            return i
    return -1