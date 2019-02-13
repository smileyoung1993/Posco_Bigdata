#2

# 중간고사와 기말고사 점수를 입력받아 평균과 학점을 구하는 프로그램

# 평균 구하는 함수
def avg(x,y):

    result = (x+y)/2

    return result

# 학점을 구하는 함수

def grade(avg_score):

    if avg_score >= 90:
        print("Grade : A")
    elif avg_score >= 80 and avg_score < 90:
        print("Grade : B")
    elif avg_score >= 70 and avg_score < 80:
        print("Grade : C")
    elif avg_score >= 60 and avg_score < 70:
        print("Grade : D")
    else:
        print("Grade : F")


#main

mid_score = int(input("Enter your midterm score: "))
final_score = int(input("Enter your final score: "))

result1 = avg(mid_score,final_score)
print("Average: %.1f" %result1)
grade(result1)
