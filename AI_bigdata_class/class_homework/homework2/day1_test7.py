#7

'''
양의 두 정수 a, b를 입력 받아, a부터 b까지의 정수의 합을 구하여 출력하는 프로그램을 작성하시오.
(for 또는 while을 이용할 것)
단, 조건 a <= b 을 만족하는 값만 고려한다.
'''

def sum_num(x,y):
    total_sum = 0
    for i in range(x,y+1,1):
       total_sum = total_sum + i

    return total_sum

# main
a,b = map(int,input("Enter two integers : ").split())

result = sum_num(a,b)

print("The sum from %d to %d is %d" %(a,b,result))