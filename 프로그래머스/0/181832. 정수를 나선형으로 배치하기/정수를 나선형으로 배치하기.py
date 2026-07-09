def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y, i = 0, -1, 0
    num = 1
    
    while(num < n**2+1):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < n) and (0 <= ny < n) and (answer[nx][ny] == 0):
            answer[nx][ny] = num
            num += 1
            x += dx[i]
            y += dy[i]
        
        else:
            i = (i + 1) % 4
    
    return answer