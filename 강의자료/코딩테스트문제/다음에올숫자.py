# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

# 제한사항

# 2 < common의 길이 < 1,000
# -1,000 < common의 원소 < 2,000
# 등차수열 혹은 등비수열이 아닌 경우는 없습니다.
# 공비가 0인 경우는 없습니다.




def solution2(common):
    if common[1] + (common[1]-common[0]) == common[2]:
        answer = common[len(common)-1]+(common[1]-common[0])
    else:
        answer = common[len(common)-1]*(common[1] // common[0])
    return answer




def solution(common):
    num = common[1]-common[0]
    if common[1] + num == common[2]:
        answer = common[len(common)-1]+num
    else:
        num = common[1] // common[0]
        answer = common[len(common)-1]*num
    return answer
    
print(solution(	[1, 2, 3, 4]))
print(solution2(	[1, 2, 3, 4]))
print(solution(	[1, 2, 4]))
print(solution2(	[1, 2, 4]))
