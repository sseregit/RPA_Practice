import pyautogui
# 이미지로 저장한것의 위치를 찾아서 return 못찾으면 None
file_menu = pyautogui.locateOnScreen("제목 없음.png")
print(file_menu)
pyautogui.click(file_menu)

# 같은 이미지가 여러개 있을경우 모두 찾을때.
file_menu = pyautogui.locateAllOnScreen("제목 없음.png")
for i in file_menu:
    print(i)
    pyautogui.click(i, duration=0.25)


# 속도 개선
# 1. GrayScale / 이미지를 흑백으로 전환해서 빠르게찾음, 정확도는 조금 떨어짐
top_arrow = pyautogui.locateOnScreen("top_arrow.png", grayscale=True)
pyautogui.moveTo(top_arrow)

# 2. 범위 지정 / x , y , width, height
top_arrow = pyautogui.locateOnScreen("top_arrow.png", region=(1817,628, 1911-1817, 713-628))
pyautogui.moveTo(top_arrow)

# 3. 정확도 조정
# pip install opencv-python 이 필요함.
top_arrow = pyautogui.locateOnScreen("top_arrow.png", confidence=0.9)
pyautogui.moveTo(top_arrow)


# 자동화 대상이 바로 보여지지 않는 경우
file_menu_notepad = pyautogui.locateOnScreen("notepad_file.png")

# 1. 발견이 될때 까지 작업하기.
if file_menu_notepad:
    pyautogui.moveTo(file_menu_notepad)
else:
    print("발견 실패")

# 발견 될때까지 반복
while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen("notepad_file.png")
    print("발견 실패")

pyautogui.moveTo(file_menu_notepad)

# 2. 일정 시간동안만 기다리기 (Timeout)
import time
import sys

file_menu_notepad = pyautogui.locateOnScreen("notepad_file.png")
file_menu_notepad = None
timeout = 10 
# 시작 시간 설정
start = time.time()
while file_menu_notepad is None:
    file_menu_notepad = pyautogui.locateOnScreen("notepad_file.png")
    end = time.time()
    if end - start > timeout:
        print("시간종료")
        # 프로그램 종료
        sys.exit() 

pyautogui.moveTo(file_menu_notepad)
       

def find_target(img_file, timeout=30):
    # 시작 시간 설정
    start = time.time()
    target = None    
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

# function으로 만들기
def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program")
        sys.exit()

my_click("notepad_file.png", 10)


        
