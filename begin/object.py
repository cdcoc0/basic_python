# #마린: 공격 유닛, 군인, 총 사용 가능
# name = "마린"
# hp = 40
# damage = 5

# #탱크: 공격 유니ㅛ, 탱크, 포 사용 가능, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격한다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)


#일반 유닛(부모)
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동. [속도 {2}]".format(self.name, location, self.speed))

#인스턴스 생성
# marine1 = Unit("marine", 40, 5)
# marine2 = Unit("marine", 40, 5)
# tank = Unit("tank", 150, 35)
# tank.clocking = True
# if tank.clocking == True: 
#     print("유닛 이름: {0}, 공격력: {1}".format(tank.name, tank.damage))

#__init__: 생성자

#Unit 클래스 상속(자식)
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군 공격. [공격력: {2}]"\
            #self: 클래스 멤버변수, 그냥 location: 전달받은 값
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0}: {1} 데미지".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴".format(self.name))

# firebat1 = AttackUnit("firebat", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

#드랍십: 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송(이게 뭐야ㅠ.ㅠ), 공격 불가

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))


#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    #멤버변수 초기화
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드 = 0
        #super().__init__(name, hp, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


#발키리...
# valkyrie = FlyableAttackUnit("val", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

#벌쳐...ㅠㅠ 예시 좀 바꿨으면......
#vulture = AttackUnit("vul", 80, 10, 20)

#배틀크루저
# battle = FlyableAttackUnit("bat", 500, 25, 3)

# vulture.move("11시")
# battle.move("9시")


#건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #pass: 암것도 안하고 넘어가는...
        # Unit.__init__(self, name, hp, 0)
        # self 필요 없음
        super().__init__(name, hp, 0)
        self.location = location

#서플라이 디폿..
# supply = BuildingUnit("sup", 500, "7시")

# def game_start():
#     print("새로운 게임 시작")

# def game_over():
#     pass

# game_start()
# game_over()
