import pyautogui

# 절대 좌표로 마우스 이동
# 지정한 위치로 마우스(x,y)를 이동한다.
pyautogui.moveTo(200, 100)
# 0.25초 동안 100, 200 이동
pyautogui.moveTo(100, 200, duration=2)

pyautogui.moveTo(100,100, duration=2)
pyautogui.moveTo(200,200, duration=2)
pyautogui.moveTo(300,300, duration=2)

# 상대 좌표로 이동(현재 커서가 있는 위치로 부터)
# 있는 위치에서 +100 , +100 이동
pyautogui.move(100,100,duration=0.25)
# 현재 마우스 위치
print(pyautogui.position())
pyautogui.move(100,100,duration=0.25)
print(pyautogui.position())
