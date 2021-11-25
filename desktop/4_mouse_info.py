import pyautogui
# 화면에 꼭짓점으로 마우스를 보내면 동작이 멈춘다.
# 하지만 FAILSAFE = False 옵션을 주면 멈추기않고 동작을 계속한다. 사용자제
pyautogui.FAILSAFE = False
# 모든 동작에 1초씩 sleep 적용
pyautogui.PAUSE = 1
# 프로그램
pyautogui.mouseInfo()
