from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active

img = Image("xlsx/star.png")

# C3위치에 img를 삽입
ws.add_image(img, "C3")

wb.save("xlsx/sample_image.xlsx")