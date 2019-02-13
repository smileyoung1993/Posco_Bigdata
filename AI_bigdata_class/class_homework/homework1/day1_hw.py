#1 변수

a = 5
b = 8

result = a * b

print("%d * %d = %d"%(a,b,result))


#2
# 변수 할당
x = 10
y = 20

# 교환 전 x,y 출력
print("Before - x: %d , y: %d" %(x,y))

# 값 바꾸기
temp = x
x = y
y = temp

# 교환 후 x,y 출력

print("After - x: %d, y: %d" %(x,y))

'''
#3 문자열

a = 100 # 정수
s1 = "200" # 문자열(큰 따움표)
s2 = '300' # 문자열(작은 따옴표)

print(s1 + s2) #문자열 합치기

# int형으로 형변환
#s1 = int(s1)
#s2 = int(s2)
print(int(s1)+int(s2))


# 4
print("수학 점수는 %d 점 이다." %90)

# 문자열 합치기 +
print("life" + "is" + "too short")

# 문자열 곱하기 *
print("python" * 3) # 문자열 3번 반복

# 문자열 내에 변수의 값을 출력하고 싶으면 %
print("I eat %d apples." %3)

number = 10
day = "three"
print("I ate %d apples, so I was sick for %s days." % (number,day))

# %s 는 어떤 형태든 대입이 가능
#(%s는 자동으로 % 뒤의 값을 문자열로 치환)

print("I eat %s apples." % 3)

# 코드 채우기
price = int(input("상품의 가격 입력: "))
print("상품의 가격은 %d 원입니다." %price)

# 문자열 길이 구하기 : len()함수이용

s = "python"
print(len(s)) # 6

# 문자열 indexing, slicing 활용
s = 'Mission Impossible'
print(s[10:13])

s1 = "red apple"
s2 = "yellow banana"
s3 = s1[0:4] + s2[7:] # 띄어쓰기까지 포함
print(s3)

s4 = s2[0:7] + s1[4:]
print(s4)

# 산술연산자
# 2버전 에서의 5/2 : 2
# 3버전 에서의 5/2 : 2.5
'''

# 문자열 함수

# 대문자/소문자의 변환
