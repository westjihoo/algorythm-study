# https://school.programmers.co.kr/learn/courses/30/lessons/49189

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for x, y in edge :
        graph[x].append(y)
        graph[y].append(x)

    distance = [ 0 for _ in range(n + 1)]
    distance[1] = 1

    path = [1]

    while path :
        cur = path.pop(0)
        for can_go in graph[cur] :
            if distance[can_go] == 0 :
                distance[can_go] = distance[cur] + 1
                path.append(can_go)
    
    return distance.count(max(distance))


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))
