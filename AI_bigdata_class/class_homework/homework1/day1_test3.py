#3

# 반지름, 둘레, 넓이
PI = 3.141592

radius = int(input("반지름을 입력하시오 : "))
circumference = 2 * PI * radius # 원의 둘레
area = PI * (radius ** 2) # 원의 넓이

print("원 둘레: %.2f" %circumference)
print("원 넓이: %.2f" %area)