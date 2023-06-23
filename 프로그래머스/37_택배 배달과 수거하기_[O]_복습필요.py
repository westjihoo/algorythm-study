# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    total_del = 0
    total_pik = 0
    
    deliveries.reverse()
    pickups.reverse()
    # 2 1 3 0 1
    # 0 4 0 3 0

    for i in range(n) :
        total_del += deliveries[i]
        total_pik += pickups[i]
    
        while total_del > 0 or total_pik > 0 :
            total_del -= cap
            total_pik -= cap
            answer += (n - i) * 2
    return answer

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

print(solution(cap, n, deliveries, pickups))