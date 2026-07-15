def solution(keyinput, board):
    lenx, leny = int(board[0] / 2), int(board[1] / 2)

    x, y = 0, 0
    for key in keyinput:
        if key == "up":
            nx, ny = x, y + 1
        elif key == "down":
            nx, ny = x, y - 1
        elif key == "left":
            nx, ny = x - 1, y
        elif key == "right":
            nx, ny = x + 1, y

        if (-lenx <= nx <= lenx) and (-leny <= ny <= leny):
            x, y = nx, ny
            
    return [x, y]