def solution(board, moves):
    answer = 0
    basket = []
    heigth = len(board)

    for move in moves :
        meet = False
        for h in range(heigth) :
            if board[h][move-1] != 0 and meet == False :
                meet = True
                if len(basket) != 0 :
                    poped = basket.pop()
                    if poped == board[h][move-1] :
                        board[h][move-1] = 0
                        answer += 1
                    else :
                        basket.append(poped)
                        basket.append(board[h][move-1])
                        board[h][move-1] = 0
                else :
                    basket.append(board[h][move-1])
                    board[h][move-1] = 0
        print(basket)

    return answer


board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
r = 4

print(solution(board, moves))
