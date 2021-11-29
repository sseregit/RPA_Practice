import smtplib
from email.message import EmailMessage
from account import *
from random import *

nicknames = ["유재석","박명수","정형돈","노홍철","조세호"]
email = ["sseregit@kakao.com","sseregit@naver.com","sseregitjys@gmail.com"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EAMIL_PASSWORD)

    for nickname in nicknames:
        to_email = choice(email)    
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        phone = str(randint(0000,9999)).rjust(4,"0")
        content = f"{nickname} / {phone}"
        msg.set_content(content)
        smtp.send_message(msg)
        print(f"지원자 {nickname} 님에게 지원가능 {to_email} 메일 발송완료")


