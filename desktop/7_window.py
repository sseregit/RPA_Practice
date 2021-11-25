import pyautogui

# 현재 활성화된 창 정보를 가져옴
fw = pyautogui.getActiveWindow()
# 활성화된 창의 제목정보
print(fw.title)
# 활성화된 창의 크기정보
print(fw.size)
# 창의 좌표 정보
print(fw.left, fw.top, fw.right, fw.bottom)

pyautogui.click(fw.left + 30, fw.top+20)

# 모든 활성화된 창 정보 가져오기.
for w in pyautogui.getAllWindows():
    print(w)

w = pyautogui.getWindowsWithTitle("메모장")[0]

# 활성화가 되지 않았다면
if w.isActive == False:
    # 활성화 시킨다 (창을 맨앞으로 가져옴)
    w.activate()
# 현재 최대화가 되지 않았다면
if w.isMaximized == False:
    #최대화
    w.maximize()
# 현재 최소화가 되지 않았다면
if w.isMinimized == False:
    # 최소화
    w.minimize()
# 화면 원복
w.restore()
# 윈도우 닫기
w.close()