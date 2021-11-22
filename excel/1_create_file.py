from openpyxl import Workbook
# 새 워크북을 생성한다. 엑셀파일을 만듬.
wb = Workbook()
# 현재 활성화된 sheet를 가져온다. 엑셀파일을 가져옴
ws = wb.active 
# sheet의 이름 변경
ws.title = "RPA"
# 파일을저장
wb.save("sample.xlsx")
# 파일 종료
wb.close()