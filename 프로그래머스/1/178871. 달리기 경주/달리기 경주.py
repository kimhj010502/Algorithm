def solution(players, callings):
    name_dict, rank_dict = {}, {}
    for i, player in enumerate(players):
        name_dict[player] = i
        rank_dict[i] = player
    
    for after_name in callings:
        after_rank = name_dict[after_name]
        before_name = rank_dict[after_rank-1]
        
        name_dict[after_name] = after_rank-1
        name_dict[before_name] = after_rank
        
        rank_dict[after_rank] = before_name
        rank_dict[after_rank-1] = after_name
    
    answer = []
    for i in range(len(players)):
        answer.append(rank_dict[i])
    return answer