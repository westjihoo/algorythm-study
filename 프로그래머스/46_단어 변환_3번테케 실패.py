# https://school.programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    if not target in words: return 0
    else: pass

    results = []
    dic_word = dict()

    for w in words:
        cnt = 0
        for i in range(len(begin)) :
            if begin[i] != w[i] :
                cnt += 1
            if cnt >= 2 : break
        if cnt == 1 :
            dic_word[begin] = dic_word.get(begin, []) + [w]
    # a = {'hit' : ['hot'],
    #     'hot': ['dot', 'lot'], 
    #     'dot': ['hot', 'dog', 'lot'],
    #     'dog': ['dot', 'log', 'cog'],
    #     'lot': ['hot', 'dot', 'log'],
    #     'log': ['dog', 'lot', 'cog'],
    #     'cog': ['dog', 'log']}
    for w in words:
        for w2 in words:
            cnt = 0
            for i in range(len(begin)):
                if w[i] != w2[i]:
                    cnt += 1
                if cnt >= 2 : break
            if cnt == 1:
                dic_word[w] = dic_word.get(w, []) + [w2]

    def dfs(now, path, depth) :
        if now == target :
            results.append(depth)
            return
        
        
        for k, v in dic_word.items() :
            if k == now and len(v) > 0 and not v[-1] in path:
                dfs(v[-1], path + [now], depth + 1)

    dfs(begin, [], 0)

    if len(results) == 0: answer = 0
    else: answer = min(results)

    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
