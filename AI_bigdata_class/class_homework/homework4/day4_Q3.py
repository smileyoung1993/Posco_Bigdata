# 천 단위마다 쉼표(,) 추가하는 함수 정의하기(완료)
def add_comma(val):
    lst_val = list(str(val))
    cnt = 0
    for i in range(len(lst_val) - 1, -1,-1):

        try:
            cnt += 1 # 천단위의 갯수를 센다 (3의 배수개)
            if len(lst_val) > 3:
                if cnt % 3 == 0:# 3의 배수일때
                    lst_val[i] = ',' + lst_val[i] # 해당위치에',' 추가
        except len(lst_val) <= 3 : # 천단위 이하일때
                break

    return ''.join(lst_val)

def main():
    comma_added_1234 = add_comma(1234)
    comma_added_12345678 = add_comma(12345678)
    comma_added_12 = add_comma(12)

    print(comma_added_1234)
    print(comma_added_12345678)
    print(comma_added_12)

if __name__ == "__main__":
    main()