#2

#money, price

money = int(input("투입한 돈: "))
price = int(input("물건가격 : "))

back_money = money - price # 거스름돈

num1 = back_money // 500 # 500원개수
num2 = (back_money % 500) // 100 # 100원개수

print("500원 짜리:%d 개 " %num1)
print("100원 짜리:%d 개 " %num2)