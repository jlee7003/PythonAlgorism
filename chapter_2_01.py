#chapter 2 
# 파이썬 완전 기초
# print 사용법


#기본출력
print('Python start')
print("Python start")
print('''Python start''')
print("""Python Start!""")

print() #개행

#Seperator 옵션 (구분자 옵션)

print('P','Y','T','H','O','N', sep='')
print('P','Y','T','H','O','N', sep=' ')
print('P','Y','T','H','O','N', sep=',')
print('010','7777','2345', sep='-')
print('jlee7003', 'naver.com', sep='@')

print() #개행

#End 옵션 -> 하나의 라인으로 출력하려 할때 사용

print('Welcome to', end=' ')
print('IT News', end='')
print('Website', end='')

#file 옵션
import sys 
print('Learn Python', file=sys.stdout)
print()

#format 사용(d: 3 , s :'python', f:3.13131)
print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one','two'))

print()

# %s -> 몇자리수를 차지하게 출력할것이냐
#왼쪽 공백처리
print('%10s' %('nice'))
print('%10s' %('nice1111'))
print('{:>10}'.format('nice'))
print()

#오른쪽 공백처리
print('%-10s' %('nice1111'))
print('{:10}'.format('nice'))
print()


print('{:_>10}'.format('nice'))
print('{:ㅁ>10}'.format('nice'))
print('{:@>10}'.format('nice'))
print('{:^10}'.format('nice')) # 중앙 정렬
print()

print('%5s' %('nice'))
print('%.5s' %('nice'))
print('%.5s' %('nicePython')) # 5개 까지만 절삭하기
print('%5s' %('nicePython')) # .이 없으면 5개를 확보해도 글자가 다 들어감
print('{:10.5}'.format('pythonstudy')) #공간은 10개지만 보이는 글자는 5개

print()

#%d

print('%d %d' %(1,2))
print('{} {}'.format(1,2))
print('{1} {0}'.format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))
print()

#%f
print('%f' %(3.14159212131742)) #소숫자리가 전부 출력 되는 것이 아니라 짤려서 나옴
print('%1.10f' %(3.14159212131742)) #정수부는 1자리 소숫자리는 10자리 이렇게 지정이 가능함
print('{:f}'.format(3.14134242434123))
print('{:1.10f}'.format(3.14134242434123))
print()

print('%6.2f' %(3.1242244242424))
print('%06.2f' %(3.1242244242424))
print('{:06.2f}'.format(3.13142213242) )
print()