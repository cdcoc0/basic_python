#list of python modules
#python module index



#glob: 경로 내의 폴더 / 파일 조회(윈도우 dir)
# import glob
# print(glob.glob("*.txt")) #확장자가 py인 모든 파일



#os: 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) #현재 디렉토리 표시해라

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("already exists")
#     os.rmdir(folder)
#     print("folder removed")
# else:
#     os.makedirs(folder)
#     print(folder, "folder created")

# print(os.listdir())



#time: 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))


import datetime
print("오늘 날짜: ", datetime.date.today())

#timedelta: 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난 지 100일은", today + td)