# weather = input("how's the weather today?")

# if weather == "rain" or weather == "snow":
#     print("take umbrella")
# elif weather == "dusts":
#     print("bring mask")
# else:
#     print("have a good day")

# temp = int(input("temperature?"))

# if temp >= 30:
#     print("too hot")
# elif temp >= 10 and temp < 30:
#     print("yeah")
# elif temp >= 0 and temp < 10:
#     print("little cold")
# else:
#     print("toooo cold")


# for wait in [0, 1, 2, 3, 4]:
#     print("대기번회: {0}".format(wait))

# for wait in range(5):
#     print("대기번호: {0}".format(wait))

# starbucks = ["a", "b", "c", "d"]
# for cus in starbucks:
#     print("{0}, 커피가 준비되었어요!".format(cus))


# customer = "jade"
# index = 5
# while index >= 1:
#     print("{0}, 커피요! {1}번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피 끝")

#while True

# customer = "jess"
# person = "unknown"

# while person != customer:
#     print("{0}, coffee!".format(customer))
#     person = input("name?")


# absent = [2, 5]
# for stu in range(1, 11):
#     if stu in absent:
#         continue # 실행 노노 and 계속 진행
#     print("{0}, speak out the book".format(stu))


# student = [1, 2, 3, 4, 5]
# student = [i + 100 for i in student]
# print(student)

# student = ["a", "b", "c", "d", "dfda"]
# student = [len(i) for i in student]

student = ["a", "b", "c", "d"]
student = [i.upper() for i in student]
print(student)