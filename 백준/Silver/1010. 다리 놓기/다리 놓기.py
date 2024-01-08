import sys

t = int(input())

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

result = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if n == m:
        result.append(1)
    else:
        result.append(factorial(m) // (factorial(n) * factorial(m-n)))

print(*result, sep='\n')