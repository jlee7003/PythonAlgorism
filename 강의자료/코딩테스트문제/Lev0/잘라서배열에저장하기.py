def solution(my_str, n):
    answer = []
    for i in range(len(my_str)):
      answer.append(my_str[0:n])
      my_str = my_str[n:]

    answer = [i for i in answer if i not in '']

    return answer

print(solution("abcdef121fwe3",2))