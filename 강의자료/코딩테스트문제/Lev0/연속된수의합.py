def solution(num, total):
    average = total // num
    first = average - (num-1)//2
    last = average + (num + 2)//2
    answer = []
    for i in range(first,last):
      answer.append(i)

    return answer
print(solution(5,5))