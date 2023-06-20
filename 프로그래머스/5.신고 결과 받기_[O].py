# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id : 0 for id in id_list}

    # <조건> 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
    # <해석> 형식 매개변수 report배열의 중복 원소를 제거해야 한다.
    #       set()으로 캐스팅하여 중복원소 제거
    #       ["muzi frodo","apeach frodo","muzi frodo"]
    #          ↓↓
    #       ["muzi frodo","apeach frodo"]
    for r in set(report) :
        reporter, reported = r.split()

        # <조건> k번 이상 신고된 유저는 게시판 이용이 정지되며,
        #        해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
        # <해석> k와 비교하기 위해 신고 횟수 저장 필요
        #        dictionary변수에 신고받은 사람 reported를 key로 신고받은 횟수 카운팅
        dic_report[reported] += 1

    for r in set(report) :
        reporter, reported = r.split()

        # 정지 기준 k와 신고 횟수 비교
        if dic_report[reported] >= k :

            # <조건> return 하는 배열은 id_list에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.
            # <해석> answer와 id_list의 인덱스가 같다는 의미

            # <조건> k번 이상 신고된 유저는 게시판 이용이 정지되며,
            #        해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
            # <해석> reported가 k번 이상 신고받아 정지대상이면,
            #        reporter의 인덱스를 이용해 answer로 접근하여 1 증가 
            answer[id_list.index(reporter)] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))