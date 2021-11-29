import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트입니다."
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg.set_content("다운로드하세요")
# 첨부파일 등록
# rb 읽고 바이너리로
with open("desktop/no_save.png", "rb") as f:
    # 파일의 내용, 메인타입, 서브타입, 파일네임
    # MIME type
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)

with open("excel/xlsx/scores.xlsx", "rb") as f:
    # 파일의 내용, 메인타입, 서브타입, 파일네임
    # MIME type
    msg.add_attachment(f.read(), maintype="application", subtype="xls", filename=f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EAMIL_PASSWORD)
    smtp.send_message(msg)