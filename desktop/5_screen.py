import pyautogui
# 스크린샷 찍기
img = pyautogui.screenshot()
img.save("screenshot.png")

# 해당 위치를 마우스를 가져갈때 RGB값으로 구분해야할수가있음.
# 978,40 / 64,170,242 #40AAF2
# 주어진 좌표값의 한픽셀의 값
pixel = pyautogui.pixel(978, 40)
# RGB값을 가져옴
print(pixel)
# RGB 색상의 대한 True, False return
pyautogui.pixelMatchesColor(978, 40, (64,170,24))
pyautogui.pixelMatchesColor(978, 40, pixel)