import smtplib
from account import *

# smpt 객체 생성
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    # 연결이 잘 수립되는지 확인.
    smtp.ehlo()
    # 모든 내용이 암호화되어 전송
    smtp.starttls()
    # 로그인
    smtp.login(EMAIL_ADDRESS, EAMIL_PASSWORD)
    # smtp.login("sseregit@naver.com", "qwe254879!@#")
    # 메일 제목
    subject = "test mail"
    # 메일 본문
    body = "mail body"
    # 메일의 형태
    msg = f"Subject: {subject} \n{body}"
    # 보내는 사람, 받는사람, 정해진 형식의 메시지
    smtp.sendmail(EMAIL_ADDRESS, "sseregit@kakao.com", msg)
