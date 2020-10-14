# def open_account():
#     print("a new account created")

# def deposit(balance, money):
#     print("successfully wired. deposit: {0}".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("successfully withdrawed. deposit: {0}".format(balance - money))
#         return balance - money
#     else:
#         print("withdrawed rejected. deposit{0}".format(balance))

# def withdraw_night(balance, money):
#     commission = 100

#     #tuple로 여러개의 값 반환
#     return commission, balance - money - commission

# balance = deposit(100, 22)
# print(balance)

# balance = 0
# balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)


# def profile(name, age, main_lang):
#     print("이름: {0}, 나이: {1}, 언어: {2}".format(name, age, main_lang))


# profile("hey", 22, "kor")

#가변인자
# def profile(name, age, *language):
#     print("이름: {0} 나이: {1}".format(name, age), end = " ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("a", 3, "python", "java")
# profile("b", 4, "javascript")