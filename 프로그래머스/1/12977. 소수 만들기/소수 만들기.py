def compute_is_prime(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0], is_prime[1] = False, False
    for i in range(2, n+1):
        if is_prime[i] == False:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    return is_prime
    
def solution(nums):
    is_prime = compute_is_prime(3 * max(nums))
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if is_prime[nums[i] + nums[j] + nums[k]]:
                    answer += 1
    return answer