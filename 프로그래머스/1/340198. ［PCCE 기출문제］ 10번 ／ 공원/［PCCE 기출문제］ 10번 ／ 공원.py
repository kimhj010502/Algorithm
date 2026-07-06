def solution(mats, park):
    answer = 0
    
    park_num = [ [0 for _ in range(len(park[0]))] for _ in range(len(park)) ]
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            if ( (i == 0) or (j == 0) ) and park[i][j] == "-1":
                park_num[i][j] = 1
                answer = max(answer, park_num[i][j])
                continue
        
            if park[i][j] != "-1":
                park_num[i][j] = 0
                continue
            
            if (park[i-1][j-1] == "-1") and (park[i][j-1] == "-1") and (park[i-1][j] == "-1"):
                park_num[i][j] = min([park_num[i-1][j-1], park_num[i][j-1], park_num[i-1][j]]) + 1
            else:
                park_num[i][j] = 1
            
            answer = max(answer, park_num[i][j])
            
    for i in range(len(park)):
        for j in range(len(park[i])):
            print(park_num[i][j], end="\t")
        print()
    
    print("\n\n")
    for i in range(len(park)):
        for j in range(len(park[i])):
            print(park[i][j], end="\t")
        print()

        
    mats.sort(reverse=True)
    for i in range(len(mats)):
        if answer >= mats[i]:
            return mats[i]
    return -1
