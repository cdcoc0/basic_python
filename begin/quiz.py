#1)주어진 코드를 활용, 부동산 프로그램 작성하기
#출력 예제)
#총 {}대의 매물이 있다.
#강남 아파트 매매 {가격 연도}
#마포 오피스텔 전세 {가격 연도}
#송파 빌라 월세 {가격 연도}

#[코드]
class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    #매물 정보 표시
    def show_detail(self):
        pass



class real_estate(House):
    def __init__(self, location, house_type, deal_type, price, completion_year):
        House.__init__(self, location, house_type, deal_type, price, completion_year)
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type}: {self.price} {self.completion_year}년")



# def result(lst):
#     count = 0
#     for elements in lst:
#         count += 1
#     print(f"총 {count}대의 매물이 있습니다.")



# re1 = real_estate("강남", "아파트", "매매", "10억", 2010)
# re2 = real_estate("마포", "오피스텔", "전세", "5억", 2007)
# re3 = real_estate("송파", "빌라", "월세", "500/50", 2000)

# overall = []
# overall.append(re1)
# overall.append(re2)
# overall.append(re3)
# result(overall)

# re1.show_detail()
# re2.show_detail()
# re3.show_detail()

houses = []
house1 = real_estate("강남", "아파트", "매매", "10억", 2010)
house2 = real_estate("마포", "오피스텔", "전세", "5억", 2007)
house3 = real_estate("송파", "빌라", "월세", "500/50", 2000)

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))

for house in houses:
    house.show_detail()
