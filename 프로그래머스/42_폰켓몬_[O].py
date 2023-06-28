# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    answer = len(nums) // 2
    
    dic_nums = dict()
    for n in nums :
        dic_nums[n] = dic_nums.get(n, 0) + 1

    if answer > len(dic_nums) :
        return len(dic_nums)
    else :
        return answer

nums = [3,3,3,2,2,4]
print(solution(nums))