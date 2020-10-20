# try: 
#     print("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("첫 번째 숫자 입력: ")))
#     nums.append(int(input("두 번째 숫자 입력: ")))
#     #nums.append(int(nums[0] / nums[1]))
#     #num1 = int(input("첫 번째 숫자 입력: "))
#     #num2 = int(input("두 번째 숫자 입력: "))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("value error occured")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("unknown error")
#     print(err)


# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg


# try:
#     print("한 자리 숫자 나눗셈 전용 계산기")
#     num1 = int(input("첫 번째 숫자 입력: "))
#     num2 = int(input("두 번째 숫자 입력: "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값: {0}. {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("한 자리 숫자만 가능")
# except BigNumberError as err:
#     print("error, one digit number only")
#     print(err) # __str__
# finally:
#     print("thanks for joining me")

# quiz) 동네에 항상 대기 손님이 있는 치킨집이 있다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템 제작
# 시스템 코들르 확인하고 적절한 예외처리 구문

# 조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
# 출력 메시지: "잘못된 값 입력"
# 조건2: 대기 손님이 주문할 수 있는 총 수량은 10마리로 한정
# 치킨 소진 시 사용자 정의 에러 SoldOutError 발생, 프로그램 종료
# 출력 메시지: "재고 소진"

class SoldOutError(Exception):
    def __init__(self):
        pass

chicken = 10
waiting = 1 #대기번호는 1부터 시작
while(True):
    try:
        print("[남은 치킨: {0}]".format(chicken))
        order = int(input("몇 마리?"))
        if order > chicken:
            print("out of stock")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문 완료요".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값 입력")
    except SoldOutError:
        print("out of stock")
        break