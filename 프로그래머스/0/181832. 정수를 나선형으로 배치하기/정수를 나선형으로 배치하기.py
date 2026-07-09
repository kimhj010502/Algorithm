def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    direction = [1, 0, -1, 0]
    dx = 3
    dy = 0
    
    x, y = 0, 0
    num = 1
    
    while(num < n**2 + 1):
        if (answer[x][y] == 0):
            answer[x][y] = num
            num += 1
        else:
            x -= direction[dx]
            y -= direction[dy]
            dx = (dx + 1) % 4
            dy = (dy + 1) % 4
            
        if (x + direction[dx] < 0) or (x + direction[dx] >= n) or (y + direction[dy] < 0) or (y + direction[dy] >= n):
            dx = (dx + 1) % 4
            dy = (dy + 1) % 4
            
        x += direction[dx]
        y += direction[dy]
    
    return answer