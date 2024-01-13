x = int(input())
num = 1
i = 1

while(True):
    if x >= (num + i):
        num += i
        i += 1
    else:
        break

#print('num: {0}, i: {1}'.format(num, i))
row = 1
col = i
for step in range(x - num):
    col -= 1
    row += 1

if i % 2 == 1:
    print('{0}/{1}'.format(col,row))
else:
    print('{0}/{1}'.format(row,col))