import sys

t = int(input())

def location_num(x1, y1, r1, x2, y2, r2):
    distance = (x1-x2)**2 + (y1-y2)**2
    if (x1 == x2) & (y1 == y2) & (r1 == r2):
        return -1
    elif (distance > (r1+r2)**2) | ( (distance < abs(r1-r2)**2) & (r1!=r2) ): #외부 또는 내부에 존재
        return 0
    elif (distance == (r1+r2)**2) | (distance == abs(r1-r2)**2): #외접 또는 내접
        return 1
    elif abs(r1-r2)**2 < distance < (r1+r2)**2: #서로 다른 두 점
        return 2

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
    print(location_num(x1, y1, r1, x2, y2, r2))