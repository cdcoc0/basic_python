#절대값
#print(abs(-5))

#제곱: 4의 2제곱
#print(pow(4, 2))

#최댓값, 최솟값(min)
#print(max(5, 12))

#반올림
#print(round(4.99))


#from math import *
#내림
#print(floor(4.99))

#올림
#print(ceil(4.99))

#제곱근
#print(sqrt(16))


#난수
#from random import *
#print(random()) #0.0 ~ 1.0 미만의 난수
#print(random() * 10) #0.0 ~ 10.0 미만
#print(int(random() * 10))
#print(int(random() * 10) + 1) # 1 ~ 10 이하 난수

#print(int(random() * 45) + 1) # 1 ~ 45이하
#print(randrange(1, 46)) #1 ~ 46 미만
#print(randint(1, 45)) # 1부터 45이하(앞, 뒤 모두 포함)


#sen = '나는 소년이요'
#sen2 = "파이썬 공부중"
#print(sen)
#print(sen2)

#sen3 = """
#나는 소년이요
#그리고 공부중
#"""
#print(sen3)

#슬라이싱
#jumin = "393939-2938483"
#print("성별: " + jumin[7])
#print("연도: " + jumin[0:2]) #뒤의 값은 1 더해야 함
#print("월: " + jumin[2:4])
#print("일: " + jumin[4:6])
#print("생년월일: " + jumin[:6]) #처음부터 6까지
#print("뒤 7자리: " + jumin[7:]) #7부터 끝까지
#print("뒤에서부터 뒤 7자리: " + jumin[-7:])

#소문자, 대문자로 처리(lower, upper)
#python = "Yay Python"
#print(python.lower())
#print(python[0].isupper())
#print(len(python))

#replace 좋다
#print(python.replace("Python", "Java"))

#첫 번째 n
#index = python.index("y")
#print(index)
#두 번째 n
#index = python.index("n", index + 1)
#print(index )

#인덱스와 비슷하지만, 원하는 값이 없는 경우 -1 반환
#인덱스는 오류남
#print(python.find("n"))

#n이 몇 번 사용됐는지
#print(python.count("n"))


#문자열 포맷
#방법1
#print("나는 %d살" % 20) # int
#print("나는 %s 좋아" % "먹는거") # string(뿐만 아니라 다 된다)
#("Apple은 %c로 시작" % "A") # character
#print("나는 %s색, %s색을 좋아해" % ("하얀", "핑쿠"))

#방법2
#print("나는 {}살".format(20))
#순서 지정 가능
#print("나는 {1}색이랑 {0}색을 좋아해".format("하얀", "녹"))

#방법3
#print("나는 {age}살, {color}색 좋아해".format(age = 20, color = "하얀"))

#방법4
#age = 20
#color = "White"
#print(f"{age}살, {color} 좋아")


#탈출 문자: \n, \r(커서 맨 앞으로 이동해서 덮어씀),\b(백 스페이스, 문자 지우기), \t(탭)
# #따옴표 안에 따옴표: 작은따옴표 활용, \"
#print("저는 \"유유\"입니다요")

#\\: 문장 내에서 하나의 \로 사용됨


#리스트
#subway = [10, 20, 30]
#subway = ["A", "B", "C"]
#print(subway.index("A"))
#subway.append("D")
#print(subway)
#subway.insert(1, "AB")
#print(subway)
#print(subway.pop())
#print(subway)
#print(subway.count("A"))

#리스트 정렬
#num_list = [5, 2, 3, 4, 1]
#num_list.sort()
#print(num_list)

#num_list.reverse()
#num_list.clear
#num_list.extend(subway)


#사전(dictionary): Key: Val
#cabinet = {3:"A", 100:"B"}
#print(cabinet[3])
#print(cabinet.get(100))
#print(cabinet.get(4), "ho")
#print(3 in cabinet)
#키는 string 타입도 되어요

#새로운 요소 추가
# cabinet["c-20"] = 58
# print(cabinet)
# #삭제
# del cabinet["c-20"]
# print(cabinet)
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())
# cabinet.clear()

#튜플(변경 안됨)
# menu = ("hey", "ho")
# print(menu)
# (name, age, hobby) = ("디욘", 20, "코딩쓰")

#집합(set)
#중복x, 순서x
# ma_set = {1, 2, 3, 3, 3}
# print(ma_set)

# java = {"유", "김", "양"}
# python = set(["유", "박"])

# print(java & python)
# print(java.intersection(python))

# print(java | python)
# print(java.union(python))

# print(java - python)
# print(java.difference(python))

# python.add("김")
# print(python)

# java.remove("김")
# print(java)


#데이터 형 변경
# menu = {"커피", "우유", "주스"}
# print(type(menu))

# menu = list(menu)
# print(type(menu))

# menu = tuple(menu)
# print(type(menu))


