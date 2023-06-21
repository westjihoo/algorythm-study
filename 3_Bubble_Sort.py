def bubble_sort(list):
    tmp = 0
    i = 0
    n = len(list)

    # i는 0부터 n-1까지 1씩 증가하면서, 리스트 우측에 정렬이 완료된 수를 연산하지 않도록 한다.
    # 리스트의 범위를 -i만큼 줄여준다
    # □□□□□  i = 0
    # □□□□■  i = 1
    # □□□■■  i = 2
    # □□■■■  i = 3
    # □■■■■  i = 4

    while i < n :
        # 실제 정렬을 실행할 범위를 의미한다
        # n-1-i 는 리스트의 길이 n=5, i=0 일 때, 5-1-0=4 로 range(4)는 0~3이 되며
        # 실제 리스트의 5개 중, 인덱스 3번, 즉 네번째에 위치한 수를 가르킨다.
        # 이때 비교는 1칸 우측에 있는 수와 비교하므로 네번째와 다섯번째 수를 비교하여
        # 실질적으로 리스트 끝까지 비교하는 것이 된다.
        #
        # -1 가 없다면 [list index out of range] 발생
        # -i 가 없다면 불필요한 연산 발생으로 성능 저하가 발생
        for j in range(n-1-i) :
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp
        i += 1
    return list

list_a = [12,16,1,3,22,53,4]
print(bubble_sort(list_a))
