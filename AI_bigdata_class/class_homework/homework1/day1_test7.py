#7

#10년후의 날짜 알아보자

year,month,day = input("날짜(연/월/일)입력 : ").split('/') # 문자 / 를 기준으로 3개의 문자열을 나눠 3개의 변수에 저장
print(type(year))
print("입력한 날짜의 %d년 후는 %d 년 %s 월 %s 일" %(10,int(year)+10,month,day))