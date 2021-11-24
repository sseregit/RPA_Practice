from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# 해당 index에 row 삽입
ws.insert_rows(8)
# 해당 index 로부터 5줄이 삽입
ws.insert_rows(9, 5)
# B번재 열이 비워지고 새로운 열이 생긴다.
ws.insert_cols(2)
# B번째 열부터 3칸을추가
ws.insert_cols(3,5)


wb.save("sample.xlsx")