#4
#평균과 분산을 구하자
# lambda(x : sum(x),lst_v)
def mean_and_var(*val):
    lst_v = list(zip(*val))# 리스트로 받음(같은 위치의 원소끼리 묶어줌)
    #평균
    mean_val = tuple(map(lambda x:sum(x)/3,lst_v))
    #분산
    var1_val = 0
    var2_val = 0
    for i in range(0,len(lst_v)):
        for j in lst_v[i]:
            var1_val += ((j - mean_val[i]) ** 2) / 3
            var2_val += ((j - mean_val[i]) ** 2) / 3

    return mean_val,(var1_val,var2_val)

def main():
    v1 = (0,1)
    v2 = (0.5,0.5)
    v3 = (1,0)

    m,v = mean_and_var(v1,v2,v3)
    print('평균:',m,'분산:',v)

if __name__ == '__main__':
    main()