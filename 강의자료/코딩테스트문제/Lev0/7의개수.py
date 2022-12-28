def solution(array):
    answer = ''.join(map(str, array)).count("7")
    return answer


print(solution([7,77,17]))