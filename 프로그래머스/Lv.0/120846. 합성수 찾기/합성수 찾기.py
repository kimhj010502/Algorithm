#소수 여부 배열 반환 (소수면 합성수)
def isPrime(n):
    prime = [True] * (n + 1) #prime[i]: i가 소수인지의 여부
    prime[0] = prime[1] = False
    
    i = 2
    while (i * i <= n):
        #i가 소수가 아닌 경우 넘어감
        if (not prime[i]):
            i += 1
            continue
        
        #i가 소수인 경우 i의 배수는 다 소수가 아님
        for j in range(2 * i, n + 1, i):
            prime[j] = False
        i += 1
            
    return prime

def solution(n):
    return n - sum(isPrime(n)[2:]) - 1