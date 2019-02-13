
#1

#입력받은 정수가 짝수인지 홀수인지 판별

def number_distict(x):

    if x % 2 == 0:
        print("%d is Even number" %x)
    else:
        print("%d is Odd number" %x)


#main

number = int(input("Enter a number : "))

number_distict(number)