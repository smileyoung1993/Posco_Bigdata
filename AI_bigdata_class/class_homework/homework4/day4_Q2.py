# prime number(소수)
def check_prime(num):
    # 1과 자기자신만 약수로 갖는 수 (2부터시작)
    for i in range(2,num):
        if num % i == 0: # 약수가 하나라도 있으면 소수가아니다
            return False
    return True # 자기보다 작은수중 약수가 없으면 소수

def main():
    a = 2
    b = 15

    if check_prime(a):
        print(str(a)+'는 소수입니다.')
    else:
        print(str(a)+'는 소수가 아니옵니다.')

    if check_prime(b):
        print(str(b)+'는 소수입니다.')
    else:
        print(str(b)+'는 소수가 아니옵니다.')

if __name__ == "__main__":
    main()