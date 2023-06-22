# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):

    w, h = len(wallpaper[0]), len(wallpaper)
    answer = [None, None, None, None]

    for h_idx in range(h) :
        for w_idx in range(w) :
            if wallpaper[h_idx][w_idx] == '#' :
                if answer[0] is None :
                    answer[0] = answer[2] = h_idx
                if answer[1] is None :
                    answer[1] = answer[3] = w_idx
                if h_idx <= answer[0] and answer[0] is not None :
                    answer[0] = h_idx
                if w_idx <= answer[1] and answer[1] is not None :
                    answer[1] = w_idx
                if h_idx >= answer[2] and answer[2] is not None :
                    answer[2] = h_idx + 1
                if w_idx >= answer[3] and answer[3] is not None :
                    answer[3] = w_idx + 1
                    
    return answer

wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...." ]
wallpaper = [".#...", "..#..", "...#."]
# result = [0, 0, 7, 9]

print(solution(wallpaper))