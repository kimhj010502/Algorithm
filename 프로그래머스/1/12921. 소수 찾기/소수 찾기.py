def get_prime_num(n):
    is_prime = [0, 0] + [1 for _ in range(n-1)]
    for num in range(2, (n+1)//2):
        for i in range(num*2, n+1, num):
            is_prime[i] = 0
            i *= num
    return is_prime

def solution(n):
    is_prime = get_prime_num(n)
    return sum(is_prime)