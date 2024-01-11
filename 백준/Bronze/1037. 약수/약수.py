import sys

n = int(input())
factor_list = list(map(int, sys.stdin.readline().rstrip().split()))
factor_list.sort()

if n == 1:
    print(factor_list[0]**2)
else:
    print(factor_list[0] * factor_list[-1])