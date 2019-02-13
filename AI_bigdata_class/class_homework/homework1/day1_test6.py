#6

# 함수선언
def sum(x,y):
    return x+y

def avg(x,y):
    result = (x+y)/2
    return result

# main

num1,num2 = map(int,input("Enter two integers: ").split())

result1 = sum(num1,num2)
result2 = avg(num1,num2)

print("The sum of %d and %d is %d" %(num1,num2,result1))
print("The average of numbers is %.1f" %(result2))

