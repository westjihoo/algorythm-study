def solution(players, callings):
    ranks = {player : i for i, player in enumerate(players)}
    index = {i : player for i, player in enumerate(players)}

    for call in callings :
        who, rank_w = call, ranks[call]
        fast, rank_f = index[rank_w-1], rank_w-1

        ranks[who] = rank_f
        ranks[fast] = rank_w

        index[rank_w] = fast
        index[rank_f] = who

    result = []
    for item in index.items() :
        result.append(item[1])

    return result

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))