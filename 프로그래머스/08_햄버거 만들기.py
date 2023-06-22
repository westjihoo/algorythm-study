# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    making = [[0]]* (len(ingredient)//4)
    cnt = 0
    print(making)
#   making = [
#       [1],
#       [1]
# ]

    for i in range(len(ingredient)) :
        if i != 0 and ingredient[i] == 1 and ingredient[i-1] == 1 :
            cnt += 1
            making[cnt].append(ingredient[i])
        elif ingredient[i] == 1 :
            making[cnt].append(ingredient[i])
        elif (ingredient[i] - 1) == ingredient[i-1] :
            making[cnt].append(ingredient[i])

    print(making)

    answer = 0
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
result = 2
# ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
result = 0

solution(ingredient)