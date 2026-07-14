def solution(board):
    safe_map = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    
    for x in range(len(safe_map)):
        for y in range(len(safe_map[x])):
            if board[x][y] == 0:
                continue
            
            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < len(board)) and (0 <= ny < len(board[0])):
                    safe_map[nx][ny] = 1

    answer = 0
    for i in range(len(safe_map)):
        for j in range(len(safe_map[i])):
            if safe_map[i][j] == 0:
                answer += 1
    
    return answer