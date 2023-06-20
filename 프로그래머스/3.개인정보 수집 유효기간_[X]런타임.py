# https://school.programmers.co.kr/learn/courses/30/lessons/150370

import datetime as dt

def solution(today, terms, privacies):

    def format_date(date) :
        return dt.datetime.strptime(date, '%Y.%m.%d')

    #slice date
    # year, mon, day = today.split(".")
    dt_today = format_date(today)

    answer = []
    dic_term = {}
    for term in terms :
        term_type, term_expiry = term.split()
        dic_term[term_type] = term_expiry
    # {'A': '6', 'B': '12', 'C': '3'}

    arr_privacy = []
    for privacy in privacies :
        date, p_type = privacy.split()
        arr_privacy.append([date,p_type])

    i = 0
    while i < len(privacies) :
        month = int(dic_term[arr_privacy[i][1]])
        year, mon, day = arr_privacy[i][0].split(".")
        year, mon = int(year), int(mon)
        mon += month
        if mon > 12 : 
            year += 1
            mon -= 12
        arr_privacy[i][0] = format_date(f'{year}.{mon}.{day}')
        
        if arr_privacy[i][0] <= dt_today :
            answer.append(i+1)
        i += 1

    return answer

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
# today = "2022.05.19"
# terms = ["A 6", "B 12", "C 3"]
# privacies  = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


print(solution(today,terms,privacies))