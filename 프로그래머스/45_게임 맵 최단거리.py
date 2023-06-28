def solution(maps):
    answer = -1
    # [
    #     [1,0,1,1,1],
    #     [1,0,1,0,1],
    #     [1,0,1,1,1],
    #     [1,1,1,0,1],
    #     [0,0,0,0,1]
    # ]
    goal_x, goal_y = len(maps[0]), len(maps)
    
    results = []
    path = []
    depth = 1
    start = [0, 0]
    goal = [goal_y - 1, goal_x - 1]
    scale = [[1,0],[0,1],[-1,0],[0,-1]]
    
    def dfs(yx, depth, path):
        if yx == goal :
            results.append(depth)
            return
        
        for x, y in scale :
            next_yx = [yx[0] + y, yx[1] + x]

            if 0 <= next_yx[0] < goal_y and 0 <= next_yx[1] < goal_y :
                if not next_yx in path and maps[next_yx[0]][next_yx[1]] == 1 :
                    depth += 1
                    path.append(yx)
                    dfs(next_yx, depth, path)
            else :
                pass
    
    dfs(start, depth, path)

    if len(results) == 0 :
        return -1
    else :
        answer = min(results)
    
    return answer


maps = [
        [1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]
    ]

print(solution(maps))