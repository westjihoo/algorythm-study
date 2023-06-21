# https://school.programmers.co.kr/learn/courses/30/lessons/150368

from itertools import product

def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    answer = []

    for case in product(discount, repeat=len(emoticons)) :
        print(case)

    return answer



# users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
# emoticons = [1300, 1500, 1600, 4900]
# result = [4, 13860]

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
result = [1, 5400]

print(solution(users, emoticons))