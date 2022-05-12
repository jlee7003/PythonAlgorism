#chapter 2-02
#파이썬 완전 기초
#파이썬 변수 

#기본 선엉

n = 700 #700을 n에 할당하는 것 
print(n)
print(n*400)
print(type(n)) #n의 자료형 출력 


# 동시 선엉

x = y = z =700
print(x,y,z)

#재선언
var = 70

var = 'Change value'

print(var)
print(type(var))


#object references
#변수의 값 할당 상태
#1. 타입에 맞는 오브젝트 생성
#2. 값 생상
#3. 콘솔 출력 

#예1)
print(300)
print(int(300))

#예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n 
print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

#ID(identity) - 객체의 고유값 확인 

print(id(m)) # 오브젝트의 고유값 출력
print(id(n)) 
print(id(n) == id(m)) 
print()


# 같은 오브젝트 참조
m = 800
n = 800
z = 800
i = 800

print(id(m)) # 오브젝트의 고유값 출력
print(id(n)) 
print(id(n) == id(m)) 
print(id(n) == id(m) == id(n) == id(m))
 # 각 오브젝트의 id 값이 달라야 맞을거 같은데 결과값을 보면 false다 왜 그럴까?
 # 그 이유는 파이썬 인터프립터(파이썬 머신)가 효율성을 위해 하나의 오브젝트로 처리하기 때문이다

print()

#다양한 변수 선언 법
#Camel Case : 처음에는 소문자로 시작하고 연결 되는 단어 부터 대문자를 쓰는것
#Pascal Case : NumberOfCollegeGraduates 전부 대문자 -> 클래스를 선언할때 주로 사용 변수 선언을 할때 사용하지 않는 것이 좋다
#Snake Case : number_of_college_graduates

#허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age =6
age =7
age_= 8 
_AGE_ = 9 
#1AGE = 1 -> 숫자로 시작하는 변수를 선언하면 에러가 남

#예약어
# -> 이미 파이썬에서 사용하는 단어들로는 변수 선언이 불가능하다
#for = 1
#as = 3
#class = 5