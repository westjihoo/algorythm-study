# 1. 이중배열로 grid를 표현해야 한다.
# 2. dirs = {"N":(-1,0), "S":(1,0), "E":(0,1), "W":(0,-1)}
#    방향에 따른 row, col 변화를 미리 저장
# 3. new_h, new_w = (curr_h + dir_h * offset), (curr_w + dir_w * offset) 
#    검사는 new_ 로 진행한다
# 4. loop와 offset 이용해서 이동경로의 상태를 확인한다 

def solution(park, routes) :
    w, h = len(park[0]), len(park)
    grid = [[0 for w_idx in range(w)] for h_idx in range(h)]
    curr_h, curr_w = 0, 0

    for h_idx in range(h) :
        for w_idx in range(w) :
            if park[h_idx][w_idx] == 'X' :
                grid[h_idx][w_idx] = 1
            elif park[h_idx][w_idx] == 'S' :
                curr_h, curr_w = h_idx, w_idx
    
    dirs = {"N":(-1,0), "S":(1,0), "E":(0,1), "W":(0,-1)}
    for route in routes :
        direction, distance = route.split()
        dir_h, dir_w = dirs[direction]
        is_valid = True
        for offset in range(1, int(distance)+1) :
            new_h, new_w = curr_h + dir_h * offset, curr_w + dir_w * offset
            if new_h in range(h) and new_w in range(w) and grid[new_h][new_w]==0 :
                pass
            else :
                is_valid = False
                break
        if is_valid :
            curr_h, curr_w = new_h, new_w
    return [curr_h, curr_w]

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))