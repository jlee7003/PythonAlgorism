N = int(input())

score = list(map(int,input().split(' ')))

maxScore = max(score)
ans = sum(score)

tot = ans * 100 / maxScore / N


print(tot)