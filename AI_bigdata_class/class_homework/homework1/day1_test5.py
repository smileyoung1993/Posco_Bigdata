#5

# 연산과제

a,b= map(int,input("Enter two integers: ").split())
# map 을 사용하여 두개의 변수에 입력받은 사용자 값을 split하고 int로 변환하여 저장(중요!)

# 출력
print("%d + %d = %d" %(a,b,a+b))
print("%d - %d = %d" %(a,b,a-b))
print("%d * %d = %d" %(a,b,a*b))
print("%d / %d = %.1f" %(a,b,a/b))
print("%d %% %d = %d" %(a,b,a%b)) # %는 연산자 앞에 문자로 인식될 수 있게 %%
