def solution(n):
    num =  []
    for i in range(1, n) :
        print(i)
        if n % (i) == 0 :
            num.append(i)

    print(num)
    if len(num) % 2 == 0 : #제곱수라면
        return 1
    else:
        return 2


def solution2(n):
   sqrt = n **0.5
   print(sqrt)
   return 1 if sqrt == int(sqrt) else 2

print(solution2(976))