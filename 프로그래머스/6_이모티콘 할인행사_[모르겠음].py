# https://school.programmers.co.kr/learn/courses/30/lessons/150368

# <문제>
# - 1번 목표가 우선이며, 2번 목표가 그 다음입니다.
#     1. 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
#     2. 이모티콘 판매액을 최대한 늘리는 것.
# - n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매합니다.
# - 이모티콘마다 할인율은 다를 수 있으며, 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됩니다.
# - 각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매합니다.
# - 각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면,
#   이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입합니다.

# 필요 로직
#  - 할인율에 따른 가입자수, 실적 계산
#  - 
# MAX[할인율 별 가입자수]

from itertools import product

def solution(users, emoticons) :
    answer = []
    sales = [10, 20, 30, 40]
    
    for case in product(sales, repeat=len(emoticons)) :
        result = [0, 0]

        for user in users :
            tmp_total = 0

            for idx, sale in enumerate(case) :

                if sale >= user[0] :
                    tmp_total += emoticons[idx] * (100 - sale) // 100
            
            if tmp_total >= user[1] :
                result[0] += 1
            else :
                result[1] += tmp_total
            
        answer.append(result)
    
    answer.sort(key=lambda x: (-x[0], -x[1]))

    return answer[0]


# users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
# emoticons = [1300, 1500, 1600, 4900]
# result = [4, 13860]

users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
# result = [1, 5400]

print(solution(users, emoticons))