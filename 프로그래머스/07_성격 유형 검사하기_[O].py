# https://school.programmers.co.kr/learn/courses/30/lessons/118666

# 나만의 카카오 성격 유형 검사지를 만들려고 합니다.
# 성격 유형 검사는 다음과 같은 4개 지표로 성격 유형을 구분합니다. 성격은 각 지표에서 두 유형 중 하나로 결정됩니다.

# 지표 번호	성격 유형
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

# 선택지	성격 유형 점수
# 매우 비동의	네오형 3점
# 비동의	네오형 2점
# 약간 비동의	네오형 1점
# 모르겠음	어떤 성격 유형도 점수를 얻지 않습니다
# 약간 동의	어피치형 1점
# 동의	어피치형 2점
# 매우 동의	어피치형 3점

# 검사 결과는 모든 질문의 성격 유형 점수를 더하여 각 지표에서
# 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라고 판단합니다.
# 단, 하나의 지표에서 각 성격 유형 점수가 같으면,
# 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.


def solution(survey, choices):
    answer = ''
    score = [3, 2, 1, 0, -1, -2, -3]
    total = {'RT' : 0, 'CF' : 0, 'JM' : 0, 'AN' : 0}

    for i in range(len(survey)) :
        x, y = survey[i][1:], survey[i][:1]
        if x+y in total :
            total[x+y] -= score[choices[i]-1]
        else :
            total[y+x] += score[choices[i]-1]

    for t in total.items() :
        a, b = t[0][1:], t[0][:1]
        if t[1] >= 0 : answer += b
        else : answer += a

    return answer



survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
result = "TCMA"

# survey = ["TR", "RT", "TR"]
# choices = [7, 1, 3]
# result = "RCJA"

print(solution(survey,choices))