# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    dic_user_info = {id : [0,0] for id in id_list}
    dic_id_idx = {id : i for i, id in enumerate(id_list)}
    dic_idx_id = {i : id for i, id in enumerate(id_list)}
    arr_who_report = [[0 for l in range(len(id_list))] for l in range(len(id_list))]


    arr_report = []
    for r in report :
        arr_report.append(r.split())

    for rep in arr_report :
        reporter = rep[0]
        reported = rep[1]

        reporter_idx = dic_id_idx[reporter]
        reported_idx = dic_id_idx[reported]
        
        if arr_who_report[reported_idx][reporter_idx] != 1 :
            dic_user_info[reported][0] = dic_user_info[reported][0] + 1
            arr_who_report[reported_idx][reporter_idx] = 1

    for idx in range(len(id_list)) :
        id = dic_idx_id[idx]
        if dic_user_info[id][0] >= 2 :
            for i in range(len(arr_who_report[0])) :
                if arr_who_report[idx][i] == 1 :
                    dic_user_info[dic_idx_id[i]][1] += 1

    for result in dic_user_info.values() :
        answer.append(result[1])

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))