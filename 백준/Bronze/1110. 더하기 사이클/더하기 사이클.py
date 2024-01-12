first_num = input()
cycle = 1

if int(first_num) < 10:
        first_num = '0' + first_num
n = first_num

while True:
    #print('cycle #{0}: {1}'.format(cycle, n)) #과정 확인용 코드
    
    n_sum = int(n[0]) + int(n[1]) #각 자리수 합으로 새로운 숫자 구하기
    new_n = n[1] + str(n_sum)[-1] #원래 숫자의 끝자리 + 새로운 숫자의 끝자리

    #print('n_sum: {0}, new_n: {1}'.format(n_sum, new_n)) #과정 확인용 코드

    if new_n == first_num:
        break
    else:
        cycle += 1
        n = new_n

print(cycle)