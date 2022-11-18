#어떠한 자연수 N은 몇개의 연속된 자연수의 합으로 나타낼수 있다 연속된 자연수의 합으로 나타내는 가짓수를
#구하시오 예를 들면 15는 15, 7+8, 4+5+6, 1+2+3+4+5 총 4가지이다

n = int(input())
count = 1 #자연수 N 그대로 의 값
startindex = 1
endindex = 1
sum = 1 

while endindex != n:
  print("변경전:",sum,startindex,endindex,count)
  if sum == n:
    print("sum이 n과 크기가 같으므로 endindex를 오른쪽으로 이동")
    count+=1
    endindex+=1
    sum += endindex
  elif sum > n:
    print("sum이 n 보다 큼으로 startindex를 오른쪽으로 이동")
    sum -= startindex
    startindex +=1
  elif sum < n:
    print("sum이 n 보다 작으므로 endindex를 오른쪽으로 이동")
    sum += endindex
    endindex += 1
  print("변경후:",sum,startindex,endindex,count)
  print("---------------------------------------")

print(count)
