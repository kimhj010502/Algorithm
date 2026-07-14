def solution(rank, attendance):
    students = []
    for i in range(len(rank)):
        if attendance[i]:
            students.append([i, rank[i]])
            
    students.sort(key=lambda x: x[1])
    
    answer = 10000 * students[0][0] + 100 * students[1][0] + students[2][0]
    return answer