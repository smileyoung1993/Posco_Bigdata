#1
#  연산자 오버로딩

class Set:
    def __init__(self,member = []):
        self.member = member

    # def append(self,a): # 하나의 변수에 원소 추가
    #     self.a = a
    #
    # def delete(self, a):
    #     self.a = a
    def union(self, s2): # 두개 set의 합집합
        c = []
        for i in range(0,len(self.member)):

        return c

    # def intersection(self, s2): # 교집합
    #     self.s2 = s2
    # # -
    # def difference(self,s2): # 차집합
    #     self.s2 = s2


a = Set([1,2,3])
b = Set([2,3,4])

print(a.member)
print(b.member)
c = a.union(b) # a+b
print(c)
#
# d = a.difference(b) #a-b
# print(d)
#
# e = a.intersection(b) # a/b
# print(e)
