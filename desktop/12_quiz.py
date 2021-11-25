import sys
import pyautogui
import pyperclip
try:
    pyautogui.PAUSE = 1
    # 그림판 실행 + 최대화
    pyautogui.hotkey("win", "r")
    pyautogui.write("mspaint")
    pyautogui.press("enter")
    pyautogui.sleep(2)
    mspaint = pyautogui.getActiveWindow()
    if not mspaint.isMaximized:
        mspaint.maximize()

    abtn = pyautogui.locateOnScreen("A.png")
    xbtn = pyautogui.locateOnScreen("X.png")

    if abtn and xbtn:
        pyperclip.copy("참 잘했어요")
        pyautogui.click(abtn)
        pyautogui.click(200,400)
        pyautogui.hotkey("ctrl","v")
        pyautogui.click(xbtn)
        pyautogui.sleep(1)
        no_save = pyautogui.locateOnScreen("no_save.png")
        if no_save:
            pyautogui.sleep(5)
            pyautogui.click(no_save)
            mspaint.close()
except Exception:
    pyautogui.alter("자동화 수행에 실패했습니다", "경고")            
    sys.exit()

