import pyautogui

# 입력한 숫자를 countdown함
# pyautogui.countdown(3)
# print("자동화 시작")

# 내용 , 타이틀 / 확인 버튼만 있는 팝업
pyautogui.alert("자동화 수행에 실패하였습니다.", "경고")
# 확인, 취소
result = pyautogui.confirm("계속 진행 하시겠습니까?", "확인")
# OK 와 Cancel로 return
print(result)
# 사용자 입력을 받는다.
result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
# 입력하면 값이 들어오고 취소시 None return
print(result)
# 패스워드를 입력받는다.
result = pyautogui.password("비밀번호를 입력하세요","입력")
print(result)