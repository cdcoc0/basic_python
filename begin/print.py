# 띄어쓰기 없이 출력
#띄어쓰기 없이 출력
#print("python", "java", sep=",")

# 각 요소 사이에 삽입
#print("python", "java", "javascript", sep=" vs ")

# 두 명령이 한 줄에(end: 맨 마지막을 어떻게 처리할 지)
# print("python", "java", sep=",", end="?")
# print("what is this?")

# import sys
# print("Python", "Java", file=sys.stdout) #표준 출력
# print("Python", "Java", file=sys.stderr) #표준 에러

#시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(5), str(score).rjust(3), sep=":")

#은행 순번표
#001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호: " + str(num).zfill(3))

# answer = input("insert: ")
# print(type(answer)) #input은 string으로 입력받는다.
# print("입력 값 출력: " + answer)

#빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
#print("{0: >10}".format(500))

#양수인 경우 +, 음수의 경우 -표시 출력
#print("{0: >+10}".format(-500))

#왼쪽 정렬, 빈칸을 _로 출력
#print("{0:_<+10}".format(500))

#3자리마다 , 찍어주기
#print("{0:,}".format(100000000000000000000))

#3자리마다 콤마, +-부호 출력
#print("{0:+,}".format(100000000000000000000))

#3자리마다 콤마, 부호, 자리수 확보, 빈 자리는 ^
#print("{0:^<+30,}".format(100000000000000000000))

#소수점 출력
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))



#파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("math: 0", file=score_file)
# print("eng: 50", file=score_file)
# score_file.close()

#a = append
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("sci: 80\n") #줄바꿈 필요
# score_file.write("cod: 100")
# score_file.close()

#읽어오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다른 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


#pickle
#프로그램 상에서 사용하는 데이터를 파일 형태로 저장
#파일을 받아 역시 피클을 사용해 사용

#import pickle
# profile_file = open("profile.pickle", "wb") #피클은 언제나 binary로 설정, 인코딩 필요없음
# profile = {"name":"podo", "age":"18", "hobby":["soccer", "golf", "coding"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 profile_file에 저장
# profile_file.close()

#읽어오기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #파일의 정보를 데이터 형태로 불러온다
# print(profile)
# profile_file.close()

#with: 더 간단하게 파일 처리
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("studying Python")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())