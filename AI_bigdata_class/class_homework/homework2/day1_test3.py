#3
'''
학생수준평가 시험에서 영어 점수와 수학 점수가 합해서 110점 이상이면 합격이다.
단, 각 점수가 40점 미만이면 불합격이다.
영어(eng), 수학(math)점수를 입력 받아 합격여부를 출력하는 프로그램을 작성하시오.
'''
# 합격여부 판단 함수
def judgement(x,y):

    score_sum = x + y

    if score_sum >= 110:

        if x >= 40 and y >= 40:
            print("합격")

        elif x < 40:
            print("불합격: 영어 점수 부족")

        elif y < 40:
            print("불합격: 수학 점수 부족")

    else:
        print("불합격: 총합 점수 부족")

#main

eng_score = int(input("영어 점수 입력: "))
math_score = int(input("수학 점수 입력: "))

judgement(eng_score,math_score)
