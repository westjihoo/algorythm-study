# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0 for l in range(len(id_list))]
    arr_report = []
    dic_count = {who : 0 for who in id_list}
    dic_id_idx = {id : i for i, id in enumerate(id_list)}
    # dic_check = {who : 0 for who in id_list}
    dic_check = {}
        
    for r in report :
        reporter, reported = r.split()
        # if  dic_check[reporter] != reported :
        if not reporter+reported in dic_check :
            arr_report.append([reporter, reported])
            # dic_check[reporter] = reported
            dic_check[reporter+reported] = 0
            dic_count[reported] += 1

    while len(arr_report) != 0 :
        rter, rted = arr_report.pop()
        if dic_count[rted] >= k :
            answer[dic_id_idx[rter]] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))