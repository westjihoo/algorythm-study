def solution(n, computers):
    graph = { x+1 : [] for x in range(n)}
    graph = make_grape(n, computers, graph)
    answer = 0

    while graph :
        now = list(graph.keys())[0]         

        graph = dfs(graph, now)

        answer += 1
    return answer


def dfs(graph, start) :
    visited = set()
    stack = []

    stack.append(start)

    while stack :
        now = stack.pop()

        if not now in visited :
            visited.add(now)
            stack.extend(graph[now])

    for key in visited :
        if key in graph :
            del graph[key]
    return graph
    
def make_grape(n, computers, graph) :
    for i in range(n) :
        for j in range(n) :
            if computers[i][j] == 1 :
                computers[i][j] = "o"

    for i in range(n) :
        for j in range(n) :
            if i != j and computers[i][j] == "o" :
                graph[i+1] = graph.get(i+1, []) + [j+1]
    return graph

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

solution(n, computers)