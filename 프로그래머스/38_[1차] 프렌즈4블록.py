# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    
    for h in range(m) :
        tmp_arr = []
        for c in board[h] :
            tmp_arr.append(c)
        board[h] = tmp_arr

    tmp_board = board
    
    for h in range(m) :
        for w in range(n) :
            if w-1 >= 0 :
                back = board[h][w-1]
                now = board[h][w]

                if back != now :
                    tmp_board[h][w] = 0
                elif back != now and now == board[h][w+1]:
                    tmp = now
            else :
                continue
    
    for w in range(n) :
        tmp = ""
        for h in range(m) :
            if tmp == "" :
                tmp = board[h][w]
            else :
                if tmp_board[h][w] != 0 :
                    if tmp == board[h][w] :
                        board[h][w] = 1
                    else :
                        board[h-1][w] = 0
                else :
                    board[h-1][w] = 0

    print(tmp_board)
    answer = 0
    return answer

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

solution(m, n, board)