def solution(n, t):
    num = n
    for i in range(t):
      num *=2
    return num


print(solution(7,15))