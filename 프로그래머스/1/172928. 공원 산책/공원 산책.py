def get_start(park):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                return i, j
    
def solution(park, routes):
    x, y = get_start(park)
    d = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}

    for i in range(len(routes)):
        op, n = routes[i].split(" ")
        can_move = True
        nx, ny = x, y
        for j in range(int(n)):
            nx, ny = nx + d[op][0], ny + d[op][1]
            if (nx < 0) or (nx >= len(park)) or (ny < 0) or (ny >= len(park[0])) or (park[nx][ny] == "X"):
                can_move = False
                break
        if can_move:
            x, y = nx, ny
    return [x, y]