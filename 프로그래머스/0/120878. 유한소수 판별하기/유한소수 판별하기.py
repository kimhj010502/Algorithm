def get_final(a, b):
    if (a == 1) or (b == 1):
        return a, b
    for i in range(2, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            return a // i, b // i
    return a, b
    
    
def is_finite(n):
    while (n % 2 == 0):
        n = n // 2
    while (n % 5 == 0):
        n = n // 5
    if n == 1:
        return 1
    return 2
    

def solution(a, b):
    while True:
        new_a, new_b = get_final(a, b)
        if (new_a == a) and (new_b == b):
            break
        else:
            a, b = new_a, new_b
    return is_finite(b)