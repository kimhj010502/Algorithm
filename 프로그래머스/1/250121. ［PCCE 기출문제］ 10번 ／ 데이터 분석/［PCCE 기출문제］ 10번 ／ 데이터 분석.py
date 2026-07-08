def solution(data, ext, val_ext, sort_by):
    ext_list = ["code", "date", "maximum", "remain"]
    
    answer = []
    for i in range(len(data)):
        if data[i][ext_list.index(ext)] < val_ext:     
            answer.append(data[i])

    answer.sort(key=lambda x:x[ext_list.index(sort_by)])
    return answer