def solution(bandage, health, attacks):
    t, h, seq = -1, health, 0 # 현재 시간, 현재 체력, 연속 공격 시간
    at = "X"
    
    while(len(attacks)):
        t += 1
        
        if t == attacks[0][0]: # 공격
            at = "O"
            h -= attacks[0][1]
            attacks.pop(0)
            seq = 0 # 체력 회복 끊김
        else: # 공격이 없으니 체력 회복
            at = "X"
            seq += 1
            h += bandage[1]
            if seq == bandage[0]: # 연속 공격 성공
                h += bandage[2]
                seq = 0
            
            if h > health:
                h = health

        if h <= 0: # 죽음
            return -1
            
        print(f"[{t}] {h}\t{seq}\t{at}")
    return h