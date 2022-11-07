#N개의 숫자가 공백없이 써있다 1이 숫자를 모두 합해 출력하는 프로그램을 작성하시오.

inp = []
inp = list(input())
sum =0
for i in inp:
  sum = sum + int(i)

print(sum)