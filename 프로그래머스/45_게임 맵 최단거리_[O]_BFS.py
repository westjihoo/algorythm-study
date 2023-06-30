# https://school.programmers.co.kr/learn/courses/30/lessons/1844

def solution(maps):
    rect_x = len(maps[0])
    rect_y = len(maps)

    jinaon = [[-1 for _ in range(rect_x)] for _ in range(rect_y)]
    jinaon[0][0] = 1
    que = [[0,0]]
    
    nx = 0
    ny = 0
    sx = [-1, 0, 1, 0]
    sy = [0, 1, 0, -1]

    while que :
        x, y = que.pop(0)
        if x == rect_x-1 and y == rect_y-1 :
            return jinaon[y][x]

        for i in range(4) :
            nx = x + sx[i]
            ny = y + sy[i]
            
            if 0 <= nx < rect_x and 0 <= ny < rect_y and maps[ny][nx] == 1 :
                if jinaon[ny][nx] == -1 :
                    jinaon[ny][nx] = jinaon[y][x] + 1
                    que.append([nx, ny])

    return -1

maps = [[1,0,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,1,1,0,1], [0,0,0,0,1]]

print(solution(maps))