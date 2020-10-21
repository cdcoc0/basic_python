#일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))



#조조 할인
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000))



#어린이 할인
def price_child(people):
    print("{0}명 어린이 가격은 {1}원 입니다.".format(people, people * 4000))
