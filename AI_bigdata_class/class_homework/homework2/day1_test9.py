#9

'''
for 문과 range()함수를 이용하여 다음과 같이 출력되도록 작성하시오.
0 1 2 3 4 5 6 7 8 9
0 5 10 15 20 25 30 35 40 45 50
10 9 8 7 6 5 4 3 2 1
'''
#
for i in range(0,10,1):
    print(i,end=" ")

print("") # 줄바꿈

for i in range(0,11,1):
    print(i*5,end=" ")

print("")

for i in range(10,0,-1):
    print(i,end=" ")

