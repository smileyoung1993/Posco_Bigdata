#12

'''
출력하고 싶은 단을 입력하세요: 7
7 * 1 =  7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
'''
#
def gugu(select):

    for i in range(1,10,1):
        print("%d * %d = %d" %(select,i,select*i))


#main

select = int(input("출력하고 싶은 단을 입력하세요: "))

gugu(select)