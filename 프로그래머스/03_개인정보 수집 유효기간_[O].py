# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):

    def get_idx_date(date) :
        year, mon, day = date.split(".")
        year, mon, day = int(year), int(mon), int(day)
        idx = ((year)*12+mon)*28+day
        return idx

    idx_today = get_idx_date(today)
    answer = []
    dic_term = {}
    for term in terms :
        term_type, term_expiry = term.split()
        dic_term[term_type] = get_idx_date(f'0.{term_expiry}.0')

    arr_privacy = []
    for privacy in privacies :
        date, p_type = privacy.split()
        arr_privacy.append([get_idx_date(date),p_type])

    i = 0
    while i < len(privacies) :
        idx_month = int(dic_term[arr_privacy[i][1]])
        idx_priv = int(arr_privacy[i][0])
        sum = idx_priv + idx_month

        if sum <= idx_today :
            answer.append(i+1)
        i += 1

    return answer

# today = "2020.01.01"
# terms = ["Z 3", "D 5"]
# privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies  = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


print(solution(today,terms,privacies))