A = [15, 13, 10, 7, 3, 12]
S = [15,28,38,45,48,60]
# for i in range(1,len(A)):
# S[i] = S[i-1] + A[i]
H = S[4]-S[2]  
print(H)

lineN, ansN =map(int,input().split(' ')) 
lis = list(map(int,input().split(' ')))
prefix_sum = [0]
temp = 0

for i in lis:
  temp = temp + i #i를 누적해서 더하는 방식으로 합배열 만들기
  prefix_sum.append(temp)

for i in range(ansN):
  s, e = map(int,input().split(' ')) 
  print(prefix_sum[e]-prefix_sum[s-1])
print(prefix_sum)