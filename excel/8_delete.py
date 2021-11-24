from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# 해당 row를 지운다.
ws.delete_rows(6)
# 2번째 rows 부터 총 3줄 삭제
ws.delete_rows(2,3)

# 해당 column을 지운다
ws.delete_cols(2)
# 해당 column 으로 부터 2개의 열을 지운다
ws.delete_cols(1,2)

wb.save("sample8.xlsx")