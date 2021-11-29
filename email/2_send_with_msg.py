import smtplib
from account import *
from email.message import EmailMessage

# 메시지 객체
msg = EmailMessage()
# 제목
msg["Subject"] = "테스트 메일입니다."
# 보내는 사람
msg["From"] = EMAIL_ADDRESS
# 받는 사람
# 여러명에게 보낼경우 이메일1,이메일2,이메일3 ','로 구분해준다.
msg["to"] = "sseregit@kakao.com"
# 참조
msg["Cc"] = "sseregit@naver.com"
# 비밀참조
msg["Bcc"] = "sseregit@naver.com"
# 메일 본문
msg.set_content("테스트 본문 입니다.")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EAMIL_PASSWORD)
    smtp.send_message(msg)