def solution(my_string):
    list(my_string.lower()).sort()
    answer = list(my_string.lower())
    answer.sort()
    
    return "".join(answer)

print(solution("DWDAa"))