import sys

n, m = map(int, input().split())
chess = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def chess_coloring(chess):
    result1 = 0; result2 = 0
    color_list = ['W', 'B']
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if chess[i][j] != color_list[0]:
                    result1 += 1
                if chess[i][j] != color_list[1]:
                    result2 += 1
            else:
                if chess[i][j] != color_list[1]:
                    result1 += 1
                if chess[i][j] != color_list[0]:
                    result2 += 1
    return min(result1, result2)

if (n == 8) & (m == 8): #8x8인 경우
    print(chess_coloring(chess))
else: #8x8이 아닌 경우
    min_result = 64
    for i in range(n-7):
        for j in range(m-7):
            chess_cut = [row[j:j+8] for row in chess[i:i+8]] #8x8로 자르기 (최적화된 곳 찾기)
            #print(*chess_cut, sep='\n')
            chess_result = chess_coloring(chess_cut)
            #print(chess_result)
            if chess_result < min_result:
                min_result = chess_result
    print(min_result)