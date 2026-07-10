def solution(bin1, bin2):
    answer = str(bin(int(bin1, 2) + int(bin2, 2)))
    answer = answer.replace("0b", "")
    return answer