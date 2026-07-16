def solution(code):
    ret = ""
    mode = 0
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = (mode + 1) % 2
            continue
        if (mode == 0 and (idx % 2) == 0) or (mode == 1 and (idx % 2) == 1):
            ret = ret + code[idx]
    if ret == "":
        return "EMPTY"
    return ret