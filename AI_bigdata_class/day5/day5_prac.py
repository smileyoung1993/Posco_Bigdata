#객체지향

class Car :
    # speed = 0

    def __init__(self,Speed):
        self.speed = Speed
    def upSpeed(self,value):
        self.speed += value

mycar1 = Car(10)
print(mycar1.speed)

mycar1.upSpeed(30)
print(mycar1.speed)

