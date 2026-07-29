def is_op(t, op_s, op_e):
    time = int(f"{t[0]:02d}" + f"{t[1]:02d}")
    op_s_time = int(f"{op_s[0]:02d}" + f"{op_s[1]:02d}")
    op_e_time = int(f"{op_e[0]:02d}" + f"{op_e[1]:02d}")
    if op_s_time <= time <= op_e_time:
        return 1
    return 0

def get_time(t, v, com):
    mm, ss = t[0], t[1]
    if com == "prev":
        if ss < 10:
            mm -= 1
            ss += 50
        else:
            ss -= 10
    elif com == "next":
        if ss >= 50:
            mm += 1
            ss -= 50
        else:
            ss += 10
    
    if (mm < 0): # 00:00 이전
        mm, ss = 0, 0
    elif (mm >= v[0] and ss > v[1]): # video_len 이후
        mm, ss = v[0], v[1]
    return [mm, ss]
    
def solution(video_len, pos, op_start, op_end, commands):
    v, t = list(map(int, video_len.split(":"))), list(map(int, pos.split(":")))
    op_s, op_e = list(map(int, op_start.split(":"))), list(map(int, op_end.split(":")))
    t = op_e if is_op(t, op_s, op_e) else t # 오프닝
    
    for com in commands:
        t = get_time(t, v, com)
        t = op_e if is_op(t, op_s, op_e) else t # 오프닝
    return f"{t[0]:02d}:{t[1]:02d}"