def solution(polynomial):
    poly_list = polynomial.split(" + ")
    a, b = 0, 0
    for i in range(len(poly_list)):
        if "x" == poly_list[i]:
            a += 1
        elif "x" in poly_list[i]:
            a += int(poly_list[i].split("x")[0])
        else:
            b += int(poly_list[i])
    
    if a == 1:
        a = ""
    if a == 0:
        return f"{b}"
    if b == 0:
        return f"{a}x"
    return f"{a}x + {b}"