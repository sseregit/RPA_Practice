import pyautogui

# 1초 동안 (1012, 48) 좌표를 마우스 클릭
pyautogui.click(1012,48, duration=1)
# click = mouseDown + mouseUp
pyautogui.mouseDown()
pyautogui.mouseUp()
# 좌표 입력이 없다면 현재위치 클릭

# 더블클릭
pyautogui.doubleClick()
# clicks = number / number숫자만큼 클릭
pyautogui.click(clicks=2)

# 드래그 드랍
pyautogui.moveTo(100,100)# # 버튼 누른상태
pyautogui.mouseDown()
pyautogui.move(300,300)
pyautogui.mouseUp()
pyautogui.rightClick()
pyautogui.middleClick()
# 상대좌표
pyautogui.drag(300,300, duration=0.25)
# 절대좌표
# pyautogui.dragTo(300,300, duration=0.25)
pyautogui.click()
# 위방향으로 300만큼 스크롤 -300은 아래 방향으로
pyautogui.scroll(-200)