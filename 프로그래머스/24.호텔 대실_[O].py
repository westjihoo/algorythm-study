# https://school.programmers.co.kr/learn/courses/30/lessons/155651

def solution(book_time):
    
    rooms = [0 for i in enumerate(book_time)]
    
    for i in range(len(book_time)) :
        for j in range(len(book_time[i])) :
            h, m = book_time[i][j].split(":")
            t = int(h) * 60 + int(m)
            book_time[i][j] = t
    
    book_time.sort()
    book_time.reverse()
    
    while len(book_time) > 0 :
        poped = book_time.pop()
        for idx, room in enumerate(rooms) :
            if rooms[idx] <= poped[0] :
                rooms[idx] = poped[1] + 10
                break
    
    rooms = [x for x in rooms if x != 0]
    answer = len(rooms)

    return answer

book_time =[
    ["15:00", "17:00"], 
    ["16:40", "18:20"], 
    ["14:20", "15:20"], 
    ["14:10", "19:20"], 
    ["18:20", "21:20"]
]

print(solution(book_time))