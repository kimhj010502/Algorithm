def get_doll(board, move):
    for i in range(0, len(board)):
        if board[i][move-1]:
            doll = board[i][move-1]
            board[i][move-1] = 0
            return board, doll
    return board, -1
    
def solution(board, moves):
    answer = 0
    basket = []
    for move in moves:
        board, doll = get_doll(board, move)
        if doll == -1:
            continue
        if len(basket) and (doll == basket[-1]):
            basket.pop()
            answer += 2
        else:
            basket.append(doll)
    return answer