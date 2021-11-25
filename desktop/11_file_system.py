# 파일 기본
import os
# current working directory 현재 작업공간
print(os.getcwd())
# 상위 폴더 이동
os.chdir("..")
print(os.getcwd())
# 상위에 상위
os.chdir("../..")
print(os.getcwd())
# 절대경로도 줄수있음.
os.chdir("c:/")
print(os.getcwd())

# 파일 경로
# 현재 작업공간 + my_file.txt 절대경로 생성
file_path = os.path.join(os.getcwd(), "my_file.txt")
print(file_path)

# 파일 경로에서 폴더 정보 가져오기
print(os.path.dirname(r"D:\RPA_practice\desktop\my_file.txt"))
# return D:\RPA_practice\desktop\

# 파일 정보 가져오기
import time
import datetime

# 파일의 생성 날짜
ctime = os.path.getctime("11_file_system.py")
print(ctime)
# 파일의 생성 날짜를 format해준다.
print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 수정 날짜
mtime = os.path.getmtime("10_log.py")
print(mtime)
print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# 파일의 마지막 접근날짜
atime = os.path.getatime("10_log.py")
print(atime)
print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기 바이트 단위 리턴
size = os.path.getsize("10_log.py")
print(size)

# getcwd() 기준 파일 목록 가져오기
print(os.listdir())
# 하위폴더가 포함되어 있지않음.
print(os.listdir(".."))
# 하위폴더 모두 포함 목록 가져오기.
# 주어진 폴더 밑에 있는 모든 폴더, 파일 목록을 가져온다.
result = os.walk("..")
# 3가지 정보를 return 해준다
for root, dirs, files in result:
    print(root, dirs, files)

# 만약 폴더 내에서 특정 파일들을 찾으려면
name = "11_file_system.py"
result = []
for root, dirs, files in os.walk("."):
    if name in files:
        result.append(os.path.join(root,name))

print(result)

# 만약 폴더 내에서 특정 파일들을 찾으려면
import fnmatch
pattern = "*.png" # .py로 끝나는 모든 파일
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        # 이름이 패턴과 일치하면 더해줌
        if fnmatch.fnmatch(name, pattern): 
            result.append(os.path.join(root,name))
            print(result)
    print()        


# 주어진 경로가 폴더인지
print(os.path.isdir("."))
# 주어진 경로가 파일인지
print(os.path.isfile("."))

# 주어진 경로가 존재하는지?
if os.path.exists("1_env.py"):
    print("존재")
else:
    print("존재안함")

# 파일 만들기
# 빈 파일 생성
open("new_file.txt", "a").close()

# 파일명 변경 / 현재 파일명 => 변경 파일명 으로
os.rename("new_file.txt","old_file.txt")

# 파일 삭제하기
os.remove("old_file.txt")

# 폴더 만들기 / 현재 경로에 생성됨 / 절대 경로를 넣으면 절대 경로로들어감.
os.mkdir("new_folder")

# 하위 폴더를 가지는 폴더 생성 / mkdir은 불가능
os.makedirs("new_folder/a/b/c/d/e")

# 폴더명 변경
os.rename("new_folder", "old_folder")

# 폴더 지우기 / 폴더 안이 비었을 때만 삭제가능하다.
os.rmdir("old_folder")

# shell utilities
import shutil 
# 폴더 안이 비어 있지 않아도 완전 삭제 가능 모든 파일 삭제 가능
shutil.rmtree("old_folder")

import shutil 
# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기 # 원본 경로, 대상경로
shutil.copy("캡처.PNG","test_folder")
# 원본 경로 , 대상경로 (변경될 파일명까지 지정)
shutil.copy("캡처.PNG","test_folder/copied_run_btn.png")

# 원본 파일 경로 / 대상 파일 경로 반드시!
shutil.copyfile("캡처.PNG", "test_folder/copied_run_btn_2.png")
# 원본 파일 경로, 대상 폴더(파일명)
shutil.copy2("캡처.png", "test_folder/copy2.png")
# copy , copyfile : 메타 정보를 복사하지 않음
# copy2 : 메타 정보 복사 (만든 시간의 정보 등등 모두 복사)

# 폴더 복사
# 원본 폴더 경로 , 대상 폴더 경로
shutil.copytree("test_folder", "test_folder2")

# 폴더 이동
# 첫번째 arg 폴더가 두번째 arg 폴더에 밑으로 들어감
# 두번째가 없으면 rename 효과를 받는다.
shutil.move("test_folder", "test_folder2")