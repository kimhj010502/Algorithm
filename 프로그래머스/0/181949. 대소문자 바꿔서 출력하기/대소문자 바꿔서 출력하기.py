str = input()

answer = ""
for i in range(len(str)):
    if ord(str[i]) < 95: # 대문자 -> 소문자
        answer = answer + str[i].lower()
    else: # 소문자 -> 대문자
        answer = answer + str[i].upper()
print(answer)