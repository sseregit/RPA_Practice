import pyautogui
# 메모장 1개를 가져옴
w = pyautogui.getWindowsWithTitle("메모장")[0]
# 창 활성화
w.activate()

pyautogui.write("12345")
# interval로 시간을 컨트롤할수있다.
pyautogui.write("NadoCoding", interval=0.25)

# left , right 방향키, enter enter키
pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=0.25)

# 특수문자
# shift키를 누른다
pyautogui.keyDown("shift")
# 눌렀다 때는 역할
pyautogui.press("4")
# shift키를 뗀다
pyautogui.keyUp("shift")

# 조합키 (Hot key)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")
pyautogui.keyUp("ctrl")
# 위와 같은 역할을 한다. 먼저 등록한 키부터 누르고 누르고 누르는 식으로 진행
pyautogui.hotkey("ctrl", "a")

# 한글을 지원하지않음,
pyautogui.write("나도코딩", interval=0.25)
# 한글글자를 쓰는법
import pyperclip
# "나도코딩" 글자를 클립보드에 저장한다.
pyperclip.copy("나도코딩")
pyautogui.hotkey("ctrl","v")

# 자동화 프로그램 종료
# win : ctrl + alt + del 
# mac : cmd + shift + option + q