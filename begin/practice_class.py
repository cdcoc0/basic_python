class Unit():
    def __init__(self):
        print("Unit 생성자")

class Flyable():
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        #맨 처음 상속받는 클래스(unit)만 초기화
        super().__init__()

#드랍십
drop = FlyableUnit()
#unit 생성자 출력