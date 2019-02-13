import random as rd
# 최대공약수 최소공배수 구하기

# 최대공약수

def GCD(a, b=None):

    if not b: # 처음 초기값이 None 이기때문에
        return a # 처음 a 를 최대공약수로 보내고 다음을 진행

    if b > a:
        temp = a
        a = b
        b = temp

    while (b > 0):
        temp = b
        b = a % b
        a = temp

    return a


# 최대공약수
def GCDs(*args):
    first_GCD = None
    for arg in args:
        for i in arg:# if not b: # 처음 초기값이 None 이기때문에
    #     return a # 처음 a 를 최대공약수로 보내고 다음을 진행

            first_GCD = GCD(i, first_GCD)

    return first_GCD

def main():
    a = []
    for i in range(10):
        a.append(rd.randint(1,100))


    gcd_value = GCDs(a)
    # lcm_value = LCMs(a)


    print('최대공약수:',gcd_value)
    # print('최소공배수:',lcm_value) # 공부 요망

if __name__ == "__main__":
    main()