#13

# 구구단 출력2 (중첩 반복문)

#
def gugu(dan):

    for i in range(2,dan+1,1):
        print("== %d 단 ==" %i)
        for j in range(1,10,1):
            print("%d * %d = %d" %(i,j,i*j))


#main

dan = int(input("출력하고 싶은 단까지 입력하세요: "))

gugu(dan)